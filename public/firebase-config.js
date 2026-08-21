// ============================================================
//  CONFIGURACIÓN DE FIREBASE  ·  PEGA AQUÍ TUS CLAVES
// ------------------------------------------------------------
//  1. Ve a  https://console.firebase.google.com  → crea un proyecto.
//  2. Agrega una app Web (</>), copia el objeto "firebaseConfig".
//  3. Reemplaza los valores de abajo con los tuyos y guarda.
//
//  Mientras diga "PEGA_AQUI...", la web funciona en MODO LOCAL
//  (el quiz sirve para estudiar, pero NO registra el avance).
//  Al pegar tus claves reales, empieza a guardar en tiempo real.
// ============================================================

export const firebaseConfig = {
  apiKey:            "PEGA_AQUI_TU_API_KEY",
  authDomain:        "PEGA_AQUI.firebaseapp.com",
  projectId:         "PEGA_AQUI",
  storageBucket:     "PEGA_AQUI.appspot.com",
  messagingSenderId: "PEGA_AQUI",
  appId:             "PEGA_AQUI"
};

// Opcional: restringe el registro a un dominio institucional.
// Deja "" para permitir cualquier correo. Ej: "@universidad.edu.co"
export const DOMINIO_INSTITUCIONAL = "";
