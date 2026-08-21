// Configuración de Supabase (base de datos en tiempo real).
// Ya está lista y conectada — no necesitas cambiar nada.
export const SUPABASE_URL = "https://sxyfswxgfcjzwnqfsqfr.supabase.co";
export const SUPABASE_KEY = "sb_publishable_lJ9dSh1LXyrmXTRr87XDpw_KuJeklB7";
export const TABLA = "avances_corazon";
export const TABLA_RESP = "avances_respiratorio";
export const TABLA_DIG = "avances_digestivo";
export const TABLA_S4 = "avances_soi2_s4";   // Semana 4 · Anatomía renal + caso de falla renal
export const TABLA_S5 = "avances_soi2_s5";   // Semana 5 · Cerebro (SN I) + caso de ACV
export const TABLA_S6 = "avances_soi2_s6";   // Semana 6 · Cerebro interno (SN II) + caso Fotoprotección
export const TABLA_S7 = "avances_soi2_s7";   // Semana 7 · Anatomía del cuello + caso de hipotiroidismo

// Opcional: restringe el registro a un dominio institucional.
// Deja "" para permitir cualquier correo. Ej: "@universidad.edu.co"
export const DOMINIO_INSTITUCIONAL = "";
