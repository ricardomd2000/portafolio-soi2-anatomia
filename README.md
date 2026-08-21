# 🫀 Portafolio de Anatomía — SOI II

Plataforma interactiva de aprendizaje y evaluación formativa en anatomía para los estudiantes de **Sistemas Orgánicos Integrados II (SOI II)** de la Facultad de Medicina de la Universidad de La Sabana.

## 🚀 Módulos y Semanas

- **Semana 1:** Corazón (corazon.html)
- **Semana 2:** Tórax y Sistema Respiratorio (
espiratorio.html, juego_respiratorio.html)
- **Semana 3:** Sistema Digestivo (digestivo.html) + Caso Clínico Virtual Laura (paciente_digestivo.html)
- **Semana 4:** Sistema Renal (
enal.html)
- **Semana 5:** Sistema Nervioso I - Cerebro y ACV (cerebro.html) con minijuego **Cerebro Arcade** (rcade/)
- **Semana 6:** Sistema Nervioso II - Cerebro Interno y Fotoprotección (semana6.html)
- **Semana 7:** Anatomía del Cuello e Hipotiroidismo (cuello.html)
- **Solución de dudas:** soluciones.html
- **Consulta de notas:** 
otas.html
- **Panel Docente:** dashboard.html (seguimiento en tiempo real y calificación)

## 🛠️ Stack Tecnológico

- **Frontend:** HTML5, CSS3, JavaScript vainilla (SPA estática).
- **Base de Datos & Tiempo Real:** Supabase (PostgreSQL, RLS y suscripciones Realtime).
- **Despliegue:** Netlify.

## 📦 Estructura del Proyecto

`
practica_corazon/
├── public/                 # Archivos web estáticos listos para producción
│   ├── index.html          # Portal principal del estudiante
│   ├── dashboard.html      # Panel docente con métricas en tiempo real
│   ├── notas.html          # Consulta individual de calificaciones
│   ├── soluciones.html     # Respuestas a dudas y videos de apoyo
│   ├── arcade/             # Minijuego interactivo Cerebro Arcade
│   ├── img/                # Imágenes de modelos anatómicos y disecciones
│   └── recursos/           # Guías descargables en PDF/DOCX
├── netlify.toml            # Configuración de despliegue en Netlify
└── README.md
`
