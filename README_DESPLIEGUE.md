# Despliegue — Corazón SOI II (Netlify + Supabase)

## Estado actual (ya hecho por mí)

✅ **Base de datos en tiempo real: LISTA y funcionando** (Supabase)
- Proyecto: `diplomado-salud-ia` · tabla `avances_corazon` con RLS y realtime activados.
- URL y clave ya están puestas en `public/supabase-config.js` — no tienes que tocar nada.
- Probada: acepta escrituras y lecturas correctamente.

✅ **Código adaptado a Supabase y validado** (`index.html` + `dashboard.html`).

✅ **Sitio de Netlify creado:** `corazon-soi2-practica` → `https://corazon-soi2-practica.netlify.app`

⛔ **Falta un solo paso: subir los archivos a Netlify.**
No pude completarlo desde mi entorno porque mi sandbox no tiene salida de red hacia la
API de despliegue de Netlify (descargó el paquete, pero la subida falló con `fetch failed`).
Ese último salto lo haces tú en ~1 minuto, sin programar nada. Aquí están las 2 formas.

---

## Opción A — Arrastrar y soltar (sin terminal, la más fácil)

1. Entra a **https://app.netlify.com/drop**
2. Arrastra la carpeta **`public`** (la que está dentro de `practica_corazon`) a la zona de la página.
3. En segundos te da una URL pública. ¡Listo!

> Esto crea un sitio nuevo con nombre aleatorio. Si prefieres usar el sitio que ya creé
> (`corazon-soi2-practica`), entra a ese sitio en Netlify → pestaña **Deploys** →
> arrastra la carpeta `public` ahí.

## Opción B — Un comando (si tienes Node instalado)

Desde la carpeta `practica_corazon`:

```bash
npx netlify-cli deploy --dir=public --prod
```

La primera vez te pedirá iniciar sesión en el navegador y elegir el sitio
`corazon-soi2-practica`. Al terminar imprime la URL en vivo.

---

## Enlaces una vez desplegado

- **Estudiantes:** la URL que te dé Netlify (ej. `https://corazon-soi2-practica.netlify.app`)
- **Panel docente (solo para ti):** esa misma URL + `/dashboard.html`

Comparte solo la primera con los estudiantes. El panel muestra la lista de avances.

---

## Cómo funciona

- El estudiante entra, va a **Repaso**, escribe **nombre + correo institucional** y estudia.
- Cada respuesta se guarda en Supabase (tabla `avances_corazon`, un registro por correo).
  Su avance se **acumula entre sesiones**: si vuelve otro día, retoma su progreso.
- El **panel docente** se actualiza **en vivo** (sin recargar): estudiantes, % de aciertos,
  respuestas, rondas y última actividad, con buscador, "activos ahora" y exportación a CSV.

Ver los datos también en Supabase: consola del proyecto → **Table Editor** → `avances_corazon`.

---

## Notas

- El banco tiene **48 preguntas**; cada ronda muestra un subconjunto distinto y baraja las opciones.
- Sin conexión a Supabase, la web sigue sirviendo como recurso de estudio (modo local, sin registro).
- **Seguridad (aula abierta):** cualquiera con el enlace puede registrar su avance. Suficiente
  para un curso. Si quieres restringir a tu dominio, pon tu dominio en `DOMINIO_INSTITUCIONAL`
  dentro de `supabase-config.js` (ej. `"@universidad.edu.co"`) y vuelve a desplegar.
- Los archivos `firebase*` y `firestore*` ya no se usan (quedaron de la versión anterior); puedes ignorarlos o borrarlos.
