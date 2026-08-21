# Portafolio de Anatomía · SOI II — Enlaces y notas

## 🔗 Enlaces del sitio (nombre actual: portafolioanatomia2026)

- **Estudiantes (inicio / portafolio):**
  https://portafolioanatomia2026.netlify.app/
  - Semana 1 · Corazón → https://portafolioanatomia2026.netlify.app/corazon
  - Semana 2 · Respiratorio → https://portafolioanatomia2026.netlify.app/respiratorio

- **Paneles docentes (solo para ti — no aparecen enlazados en el sitio):**
  - Semana 1 · Corazón → https://portafolioanatomia2026.netlify.app/dashboard
  - Semana 2 · Respiratorio → https://portafolioanatomia2026.netlify.app/dashboard_respiratorio

> Comparte con los estudiantes solo el enlace de inicio. Guarda para ti los dos de "dashboard".

---

## ✅ Datos: dónde viven y por qué NO se pierden al renombrar

El avance de los estudiantes (quiz, tiempo, checklists, recursos, encuestas, dudas) se guarda en
**Supabase** (la base de datos), no en Netlify. La web se conecta a Supabase con la URL y la clave
que están dentro de `public/supabase-config.js`, y esas no dependen del nombre del sitio en Netlify.

- Cambiar el nombre del sitio en Netlify **solo cambia el dominio (la URL)**.
- Los datos siguen intactos en Supabase y los paneles los siguen mostrando igual.
- Tablas en Supabase: `avances_corazon` (Semana 1) y `avances_respiratorio` (Semana 2).

---

## 🔁 Cómo actualizar el sitio (sin cambiar la URL)

1. Entra a tu sitio en Netlify → pestaña **Deploys**.
2. Arrastra ahí la carpeta **`public`** completa.
3. Recarga con **Ctrl + F5** (para saltar la caché del navegador).

> Importante: usa la pestaña **Deploys** del mismo sitio. Si arrastras en "app.netlify.com/drop"
> se crea un sitio NUEVO con otra URL.

---

## 🗂️ Estructura de archivos (dentro de `public/`)

- `index.html` → página de inicio (portafolio con las dos semanas).
- `corazon.html` → app de Semana 1 (corazón).
- `respiratorio.html` → app de Semana 2 (vía respiratoria y tórax).
- `dashboard.html` → panel docente Semana 1.
- `dashboard_respiratorio.html` → panel docente Semana 2.
- `supabase-config.js` → conexión a la base de datos (no borrar).
- `_redirects` → sin reglas (la raíz sirve el portafolio).
- `img/`, `recursos/` → imágenes y guía en PDF/Word.

---

## 👤 Login de estudiantes

- Se identifican una vez con **nombre + correo**; queda recordado en su navegador y sirve para
  ambas semanas (mismo login).
- Su progreso se recupera por el **correo**, así que si entran desde otro dispositivo, escriben el
  correo una vez y continúan donde iban.
- Botón "No soy yo / Salir" borra los datos guardados en ese navegador.
