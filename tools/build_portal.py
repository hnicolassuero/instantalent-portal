"""Genera index.html cifrando los datos de candidatos con el usuario y la contraseña.

Uso: python3 tools/build_portal.py datos.json USUARIO CONTRASENA FECHA_VENCE [salida]
- datos.json NO se sube al repositorio (contiene los datos sin cifrar).
- La contraseña nunca se guarda en el repositorio.
"""
import json, os, base64, sys
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

datos, user, pw, expira = sys.argv[1:5]
out = sys.argv[5] if len(sys.argv) > 5 else 'index.html'
aqui = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(datos, encoding='utf-8'))
d['expira'] = expira
salt, iv, it = os.urandom(16), os.urandom(12), 150000
key = PBKDF2HMAC(hashes.SHA256(), 32, salt, it).derive((user.lower() + ':' + pw).encode())
ct = AESGCM(key).encrypt(iv, json.dumps(d, ensure_ascii=False).encode(), None)
b = lambda x: base64.b64encode(x).decode()
cofre = json.dumps({'salt': b(salt), 'iv': b(iv), 'iter': it, 'data': b(ct), 'total': len(d['candidatos'])})
html = open(os.path.join(aqui, 'plantilla.html'), encoding='utf-8').read().replace('__COFRE__', cofre)
open(out, 'w', encoding='utf-8').write(html)
assert d['candidatos'][0]['n'] not in html or len(d['candidatos'][0]['n']) < 4, 'los datos quedaron sin cifrar'
print(len(d['candidatos']), 'candidatos cifrados en', out)
