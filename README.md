# Instantalent · Portal de candidatos

Portal de demostración con acceso por usuario y contraseña. Muestra candidatos de ventas, marketing, servicio al cliente y áreas administrativas en Latinoamérica y de hispanos en el mundo, clasificados por categoría, país, fuente y fecha de ingreso.

- `index.html`: el portal publicado en GitHub Pages. Los datos de candidatos van **cifrados** (AES-GCM, clave derivada de usuario + contraseña con PBKDF2); sin la contraseña no se pueden leer.
- `tools/plantilla.html`: diseño y código del portal, sin datos.
- `tools/build_portal.py`: genera `index.html` a partir de un `datos.json` (que nunca se sube aquí).

Solo se muestran datos que cada persona publicó para ser contactada (nombre público, cargo, ciudad, país y enlace a su perfil). Tratamiento de datos conforme a la Ley 1581 de 2012.
