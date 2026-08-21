# -*- coding: utf-8 -*-
import re
SRC="/sessions/jolly-practical-gauss/mnt/corazon/practica_corazon/public/respiratorio.html"
OUT="/sessions/jolly-practical-gauss/mnt/corazon/practica_corazon/public/renal.html"
h=open(SRC,encoding="utf-8").read()

h=h.replace("<title>Vía Respiratoria Baja y Tórax · SOI II · Semana 2</title>",
            "<title>Anatomía Renal · SOI II · Semana 4</title>")

h=h.replace(
""":root{
  --rojo:#0f7391; --rojo-osc:#0a4f66; --rojo-cl:#3aa0bd;
  --azul:#155e75; --crema:#f4f9fb; --tinta:#20313a; --gris:#5c6b72;
  --verde:#2e7d5b; --ambar:#c77d0a; --linea:#d9e6ea;
  --sombra:0 4px 18px rgba(15,80,102,.10);
}""",
""":root{
  --rojo:#7b1fa2; --rojo-osc:#4a148c; --rojo-cl:#ab47bc;
  --azul:#5e35b1; --crema:#f8f5fb; --tinta:#20313a; --gris:#5c6b72;
  --verde:#2e7d5b; --ambar:#c77d0a; --linea:#e5dcec;
  --sombra:0 4px 18px rgba(74,20,140,.10);
}""")

h=h.replace("<h2>🫁 Vía Respiratoria Baja y Tórax</h2>","<h2>🫘 Anatomía Renal · Riñón, uréter y vejiga</h2>")
h=h.replace('<p class="mini" style="margin:0 0 6px">SOI II · Semana 2 — Identifícate para comenzar.</p>',
            '<p class="mini" style="margin:0 0 6px">SOI II · Semana 4 — Identifícate para comenzar.</p>')

h=h.replace("""  <h1>Tráquea, Bronquios, Pulmones y Pleura</h1>
  <p>Laboratorio de Anatomía · SOI II · Semana 2 · Integración con caso de tórax inestable</p>
  <p class="mini">Paredes del tórax y vía aérea inferior</p>""",
"""  <h1>Riñón, Uréter y Vejiga</h1>
  <p>Laboratorio de Anatomía · SOI II · Semana 4 · Integración con caso de falla renal aguda</p>
  <p class="mini">Anatomía renal, nefrona, vascularización y vía urinaria</p>""")

FASE1="""<!-- FASE 1 -->
<section class="fase prep activa" id="prep">
  <h2 class="sec">🧠 Antes de entrar a la práctica</h2>
  <p class="intro">Llega dominando la anatomía del riñón, la nefrona, la vascularización renal y la vía urinaria; así la exploración y la correlación con el caso te rendirán el doble.</p>

  <div class="card">
    <h3>Resultados de aprendizaje</h3>
    <ul class="limpia">
      <li>Reconocer la situación retroperitoneal y las relaciones del riñón, uréter y vejiga.</li>
      <li>Describir el tamaño renal normal y sus cambios con el envejecimiento.</li>
      <li>Explicar el patrón de vascularización arterial y venoso del riñón.</li>
      <li>Identificar las partes de la nefrona y el aparato yuxtaglomerular.</li>
      <li>Trazar la vía urinaria desde los cálices hasta el meato uretral.</li>
      <li>Integrar la anatomía renal con el caso de falla renal aguda.</li>
    </ul>
  </div>

  <div class="card">
    <h3>Materiales para la práctica</h3>
    <ul class="limpia">
      <li>Modelos del riñón y del aparato urinario; preparaciones según disponibilidad.</li>
      <li>Atlas físico impreso y cuaderno para dibujar/rotular.</li>
      <li>Guantes, bata y EPP según norma del laboratorio.</li>
    </ul>
    <div class="nota"><b>Nota:</b> la práctica también incluye la toma de signos vitales y la exploración física renal (puñopercusión, puntos pieloureterales). Este portafolio se enfoca en la anatomía que las sustenta.</div>
  </div>

  <div class="card">
    <h3>🎬 Recursos (Lecturio · requiere inicio de sesión institucional)</h3>
    <p class="mini">Ábrelos antes de venir. Se abren en una pestaña nueva con tu usuario de la biblioteca.</p>
    <div class="recursos" id="recursos"></div>
  </div>

  <div class="card">
    <h3>🎬 Video complementario (YouTube)</h3>
    <p class="mini">Toca la tarjeta para reproducir. Muestra las maniobras de exploración renal.</p>
    <div class="videos" id="vids-yt"></div>
  </div>

  <div class="card">
    <h3>Roles del equipo</h3>
    <ul class="limpia">
      <li><b>Líder:</b> administra el tiempo y el orden de las estaciones.</li>
      <li><b>Operador:</b> manipula modelos/preparaciones con cuidado.</li>
      <li><b>Relator clínico:</b> conecta hallazgos con el caso de falla renal.</li>
      <li><b>Auditor:</b> diligencia los checklists y controla la calidad.</li>
    </ul>
  </div>
</section>

<!-- FASE 2 -->"""
h=re.sub(r"<!-- FASE 1 -->.*?<!-- FASE 2 -->", lambda m: FASE1, h, count=1, flags=re.S)

FASE2="""<!-- FASE 2 -->
<section class="fase dur" id="dur">
  <h2 class="sec">🔬 Durante la práctica</h2>
  <p class="intro">Trabaja estación por estación. Marca cada estructura al identificarla con seguridad.</p>

  <div class="card">
    <span class="tag a">Estación A</span><span class="tag tiempo">Riñón in situ</span>
    <h3>Situación, celda renal y relaciones</h3>
    <div class="check" data-chk="A">
      <label><input type="checkbox"> Situación retroperitoneal (aprox. T12–L3); derecho más bajo por el hígado</label>
      <label><input type="checkbox"> Cápsula renal, grasa perirrenal y fascia renal (de Gerota)</label>
      <label><input type="checkbox"> Glándula suprarrenal sobre el polo superior</label>
      <label><input type="checkbox"> Polos superior e inferior, bordes y caras del riñón</label>
      <label><input type="checkbox"> Hilio renal — orden de anterior a posterior: Vena, Arteria, Pelvis (VAP)</label>
      <label><input type="checkbox"> Corteza, médula, pirámides y papilas renales</label>
    </div>
    <div class="progreso"><i></i></div><div class="progtxt"></div>
    <div class="aviso">En el hilio, de adelante hacia atrás: <b>V</b>ena renal, <b>A</b>rteria renal, <b>P</b>elvis renal (regla VAP).</div>
  </div>

  <div class="card">
    <span class="tag a">Estación B</span><span class="tag tiempo">Vascularización</span>
    <h3>Arterias y venas del riñón</h3>
    <div class="check" data-chk="B">
      <label><input type="checkbox"> Arteria renal (rama de la aorta abdominal)</label>
      <label><input type="checkbox"> Secuencia: segmentaria → interlobar → arciforme (arcuata) → interlobulillar</label>
      <label><input type="checkbox"> Arteriola aferente → glomérulo → arteriola eferente</label>
      <label><input type="checkbox"> Vena renal y drenaje a la vena cava inferior</label>
      <label><input type="checkbox"> Vena renal izquierda: más larga, cruza delante de la aorta bajo la AMS</label>
      <label><input type="checkbox"> La renal izquierda recibe la suprarrenal y la gonadal izquierdas</label>
    </div>
    <div class="progreso"><i></i></div><div class="progtxt"></div>
    <div class="nota">La <b>arteriola eferente</b> sale del glomérulo: su tono regula la presión de filtración glomerular.</div>
  </div>

  <div class="card">
    <span class="tag a">Estación C</span><span class="tag tiempo">Nefrona</span>
    <h3>Nefrona e histología</h3>
    <div class="check" data-chk="C">
      <label><input type="checkbox"> Corpúsculo renal: glomérulo + cápsula de Bowman</label>
      <label><input type="checkbox"> Túbulo contorneado proximal → asa de Henle → contorneado distal → colector</label>
      <label><input type="checkbox"> Aparato yuxtaglomerular: mácula densa + células yuxtaglomerulares (granulares)</label>
      <label><input type="checkbox"> Ubicación de los corpúsculos en la corteza renal</label>
      <label><input type="checkbox"> Túbulos colectores que desembocan en la papila</label>
    </div>
    <div class="progreso"><i></i></div><div class="progtxt"></div>
    <div class="aviso">Las células yuxtaglomerulares secretan <b>renina</b>; la mácula densa “sensa” el sodio del túbulo distal para regular la TFG.</div>
  </div>

  <div class="card">
    <span class="tag a">Estación D</span><span class="tag tiempo">Vía urinaria y superficie</span>
    <h3>De los cálices a la uretra</h3>
    <div class="check" data-chk="D">
      <label><input type="checkbox"> Cálices menores (reciben las papilas) → cálices mayores → pelvis renal</label>
      <label><input type="checkbox"> Uréter y sus 3 estrechamientos (ureteropélvico, cruce ilíaco, ureterovesical)</label>
      <label><input type="checkbox"> Vejiga y trígono vesical (2 orificios ureterales + orificio uretral interno)</label>
      <label><input type="checkbox"> Uretra hasta el meato uretral externo</label>
      <label><input type="checkbox"> Anatomía de superficie: ángulo costovertebral (puñopercusión)</label>
      <label><input type="checkbox"> Puntos pieloureterales (superior, medio, inferior)</label>
    </div>
    <div class="progreso"><i></i></div><div class="progtxt"></div>
    <div class="nota">La vía urinaria <b>empieza</b> en los cálices menores y <b>termina</b> en el meato uretral externo.</div>
  </div>
</section>

<!-- FASE 3 -->"""
h=re.sub(r"<!-- FASE 2 -->.*?<!-- FASE 3 -->", lambda m: FASE2, h, count=1, flags=re.S)

# Quitar juego
h=re.sub(r'<div class="card">\s*<h3 style="margin-top:0">🎮 Juego.*?</div>\s*<h3>📝 Banco de preguntas</h3>', '<h3>📝 Banco de preguntas</h3>', h, count=1, flags=re.S)

# Integración con el caso (reemplaza el bloque de tórax que sigue tras "Banco"? No: el caso de tórax está en Fase 2 original, ya reemplazado). Añadimos card de caso al inicio de Fase 3.
h=h.replace('<h3>📝 Banco de preguntas</h3>',
"""<div class="card">
    <h3 style="margin-top:0">🔗 Integración con el caso (falla renal aguda)</h3>
    <p><b>Caso:</b> Juan Pérez, 72 años. TA 190/110, FC 110, oliguria, edemas; creatinina 4.3 mg/dL, BUN 102, K⁺ 5.2. Ecografía: riñones de <b>tamaño normal</b> con mala diferenciación corticomedular, sin obstrucción. Biopsia: arteriolas “en capa de cebolla” con necrosis fibrinoide.</p>
    <div class="flujo"><span>HTA maligna</span><span class="fl">→</span><span>Daño arteriolar (capa de cebolla)</span><span class="fl">→</span><span>Isquemia glomerular</span><span class="fl">→</span><span>↓ TFG</span><span class="fl">→</span><span>Oliguria + ↑creatinina/BUN/K⁺</span></div>
    <div class="nota"><b>Correlación anatómica:</b> el daño está en las <b>arteriolas</b> (aferente/eferente) que nutren el glomérulo; el <b>tamaño renal normal</b> apoya una falla <b>aguda</b> (en la crónica los riñones suelen estar pequeños).</div>
  </div>

  <h3>📝 Banco de preguntas</h3>""", 1)

# Exit ticket
h=h.replace(
"""    <ul class="limpia">
      <li>Una estructura que hoy dejé de confundir: __________</li>
      <li>En el caso, la dificultad respiratoria la conecto anatómicamente con: __________</li>
      <li>Dónde se acumularía sangre/líquido en el tórax de este paciente: __________</li>
    </ul>""",
"""    <ul class="limpia">
      <li>Una estructura que hoy dejé de confundir: __________</li>
      <li>El orden de la vía urinaria desde los cálices: __________</li>
      <li>En el caso, el daño renal lo conecto anatómicamente con: __________</li>
    </ul>""")

h=h.replace("<footer>Recurso de estudio · Vía respiratoria baja y tórax · SOI II Semana 2 · Uso educativo.</footer>",
            "<footer>Recurso de estudio · Anatomía renal (riñón, uréter y vejiga) · SOI II Semana 4 · Uso educativo.</footer>")

h=h.replace("import { SUPABASE_URL, SUPABASE_KEY, TABLA_RESP, DOMINIO_INSTITUCIONAL } from './supabase-config.js';",
            "import { SUPABASE_URL, SUPABASE_KEY, TABLA_S4, DOMINIO_INSTITUCIONAL } from './supabase-config.js';")
h=h.replace("const TABLA=TABLA_RESP;","const TABLA=TABLA_S4;")

h=re.sub(r"const RECURSOS=\[.*?\];", """const RECURSOS=[
  {id:"signos_vitales",t:"Signos vitales (Lecturio)",url:"https://unisabana.lecturio.com/#/course/s/106815/50927/"}
];""", h, count=1, flags=re.S)

h=re.sub(r"const YT=\[.*?\];", """const YT=[
  {id:"vYDE11i0tYk",t:"Maniobras de palpación renal"}
];""", h, count=1, flags=re.S)

h=h.replace("const TEMAS_LABEL={torax:'Pared torácica',via:'Vía aérea',pulmon:'Pulmón y pleura',caso:'Caso clínico'};",
            "const TEMAS_LABEL={macro:'Riñón, uréter y vejiga',vascular:'Vascularización renal',nefrona:'Nefrona e histología',via:'Vía urinaria',caso:'Caso: falla renal'};")

h=h.replace("const catLbl={torax:'🦴 Pared torácica',via:'🫁 Vía aérea',pulmon:'🫁 Pulmón y pleura',caso:'🩺 Caso clínico'}[p.cat];",
            "const catLbl={macro:'🫘 Riñón/uréter/vejiga',vascular:'🩸 Vascularización',nefrona:'🔬 Nefrona',via:'💧 Vía urinaria',caso:'🩺 Caso clínico'}[p.cat];")

POOL='''const POOL=[
 {id:1,cat:"macro",q:"Los riñones son órganos:",o:["Intraperitoneales","Retroperitoneales","Pélvicos","Intratorácicos"],c:1,e:"Los riñones son retroperitoneales, situados aproximadamente entre T12 y L3."},
 {id:2,cat:"macro",q:"El riñón derecho está algo más bajo que el izquierdo por la presencia de:",o:["El bazo","El hígado","El páncreas","El diafragma"],c:1,e:"El hígado desplaza hacia abajo al riñón derecho."},
 {id:3,cat:"macro",q:"La longitud normal aproximada de un riñón adulto es:",o:["4–6 cm","10–12 cm","18–20 cm","2–3 cm"],c:1,e:"Un riñón normal mide unos 10–12 cm de longitud; tiende a disminuir con el envejecimiento."},
 {id:4,cat:"macro",q:"La capa de grasa que rodea el riñón dentro de la fascia renal (de Gerota) es la grasa:",o:["Subcutánea","Perirrenal","Mesentérica","Epiploica"],c:1,e:"La grasa perirrenal envuelve el riñón dentro de la fascia de Gerota."},
 {id:5,cat:"macro",q:"En el hilio renal, de anterior a posterior, el orden de las estructuras es:",o:["Arteria, vena, pelvis","Vena, arteria, pelvis","Pelvis, arteria, vena","Vena, pelvis, arteria"],c:1,e:"Regla VAP: Vena renal (anterior), Arteria renal, Pelvis renal (posterior)."},
 {id:6,cat:"macro",q:"La glándula que corona el polo superior del riñón es la:",o:["Tiroides","Suprarrenal (adrenal)","Hipófisis","Paratiroides"],c:1,e:"La glándula suprarrenal se asienta sobre el polo superior de cada riñón."},
 {id:7,cat:"macro",q:"El trígono vesical está delimitado por:",o:["Los dos orificios ureterales y el orificio uretral interno","Dos orificios uretrales","El uraco y el ombligo","Los ligamentos umbilicales"],c:0,e:"El trígono vesical tiene por vértices los dos orificios ureterales y el orificio uretral interno."},
 {id:8,cat:"macro",q:"Los uréteres discurren en su trayecto abdominal:",o:["Intraperitoneales sobre el íleon","Retroperitoneales sobre el músculo psoas","Dentro del canal inguinal","Por delante del estómago"],c:1,e:"Los uréteres son retroperitoneales y descienden sobre el músculo psoas mayor."},
 {id:9,cat:"vascular",q:"La arteria renal es rama directa de:",o:["La arteria mesentérica superior","La aorta abdominal","La arteria ilíaca interna","El tronco celíaco"],c:1,e:"Las arterias renales nacen directamente de la aorta abdominal (a nivel de L1–L2)."},
 {id:10,cat:"vascular",q:"La secuencia correcta de las arterias dentro del riñón es:",o:["Interlobulillar → arcuata → interlobar → segmentaria","Segmentaria → interlobar → arciforme (arcuata) → interlobulillar","Arcuata → segmentaria → interlobar → interlobulillar","Interlobar → segmentaria → interlobulillar → arcuata"],c:1,e:"Segmentaria → interlobar → arciforme (arcuata) → interlobulillar → arteriola aferente."},
 {id:11,cat:"vascular",q:"La arteriola que ENTRA al glomérulo es la:",o:["Eferente","Aferente","Interlobulillar","Arcuata"],c:1,e:"La arteriola aferente lleva la sangre al glomérulo; la eferente la saca."},
 {id:12,cat:"vascular",q:"La arteriola que SALE del glomérulo es la:",o:["Aferente","Eferente","Interlobar","Segmentaria"],c:1,e:"La arteriola eferente drena el glomérulo; su tono regula la presión de filtración."},
 {id:13,cat:"vascular",q:"La vena renal izquierda, más larga, cruza por delante de la aorta por debajo de:",o:["La arteria mesentérica inferior","La arteria mesentérica superior","El tronco celíaco","La arteria renal derecha"],c:1,e:"La vena renal izquierda pasa entre la aorta (posterior) y la arteria mesentérica superior (anterior)."},
 {id:14,cat:"vascular",q:"A diferencia de la derecha, la vena renal izquierda recibe:",o:["La vena porta","Las venas suprarrenal y gonadal izquierdas","La vena ácigos","La vena cava inferior"],c:1,e:"La renal izquierda recibe la suprarrenal y la gonadal (testicular/ovárica) izquierdas."},
 {id:15,cat:"vascular",q:"Las venas renales drenan finalmente en:",o:["La vena porta","La vena cava inferior","La vena ácigos","La aorta"],c:1,e:"Las venas renales desembocan en la vena cava inferior."},
 {id:16,cat:"nefrona",q:"La unidad funcional del riñón es:",o:["El glomérulo","La nefrona","El cáliz","La pirámide"],c:1,e:"La nefrona es la unidad estructural y funcional del riñón."},
 {id:17,cat:"nefrona",q:"El corpúsculo renal está formado por:",o:["El túbulo proximal y el asa de Henle","El glomérulo y la cápsula de Bowman","La papila y el cáliz","La mácula densa y el túbulo colector"],c:1,e:"El corpúsculo renal = glomérulo (ovillo capilar) + cápsula de Bowman."},
 {id:18,cat:"nefrona",q:"El orden correcto del túbulo de la nefrona es:",o:["Colector → distal → asa de Henle → proximal","Contorneado proximal → asa de Henle → contorneado distal → colector","Asa de Henle → proximal → colector → distal","Distal → proximal → colector → asa"],c:1,e:"Proximal → asa de Henle → distal → túbulo colector."},
 {id:19,cat:"nefrona",q:"El aparato yuxtaglomerular incluye:",o:["Podocitos y mesangio solamente","La mácula densa y las células yuxtaglomerulares (granulares)","El túbulo colector y la papila","La cápsula de Bowman y el glomérulo"],c:1,e:"Lo forman la mácula densa (túbulo distal), las células yuxtaglomerulares (granulares) y las mesangiales extraglomerulares."},
 {id:20,cat:"nefrona",q:"Las células yuxtaglomerulares secretan principalmente:",o:["Aldosterona","Renina","ADH","Eritropoyetina"],c:1,e:"Las células yuxtaglomerulares (granulares) secretan renina, clave en la regulación de la presión y la TFG."},
 {id:21,cat:"nefrona",q:"Los corpúsculos renales (glomérulos) se ubican principalmente en la:",o:["Médula renal","Corteza renal","Pelvis renal","Cápsula"],c:1,e:"Los glomérulos están en la corteza renal; las asas de Henle y colectores profundizan en la médula."},
 {id:22,cat:"nefrona",q:"Los túbulos colectores desembocan, en el vértice de la pirámide, en:",o:["La cápsula de Bowman","La papila renal","La arteria arcuata","El hilio"],c:1,e:"Los colectores drenan en la papila renal, que vierte la orina al cáliz menor."},
 {id:23,cat:"via",q:"Anatómicamente, la vía urinaria COMIENZA en:",o:["El uréter","Los cálices menores","La vejiga","La pelvis renal"],c:1,e:"La vía urinaria empieza en los cálices menores, que reciben las papilas renales."},
 {id:24,cat:"via",q:"La secuencia correcta de la vía urinaria es:",o:["Pelvis → cálices → uréter → uretra → vejiga","Cálices menores → cálices mayores → pelvis renal → uréter → vejiga → uretra","Uréter → pelvis → cálices → vejiga → uretra","Cálices → uréter → uretra → vejiga → pelvis"],c:1,e:"Cálices menores → mayores → pelvis → uréter → vejiga → uretra."},
 {id:25,cat:"via",q:"Los cálices menores reciben la orina directamente de:",o:["El uréter","Las papilas renales (pirámides)","La vejiga","La cápsula de Bowman"],c:1,e:"Cada papila renal (vértice de una pirámide) vierte la orina en un cáliz menor."},
 {id:26,cat:"via",q:"Los 3 estrechamientos anatómicos del uréter son:",o:["Ureteropélvico, cruce de vasos ilíacos y unión ureterovesical","Pélvico, inguinal y perineal","Cortical, medular y papilar","Proximal, medio y uretral"],c:0,e:"El uréter se estrecha en la unión ureteropélvica, al cruzar los vasos ilíacos y en la unión ureterovesical (sitios frecuentes de impactación de cálculos)."},
 {id:27,cat:"via",q:"La vía urinaria TERMINA en:",o:["El trígono vesical","El meato uretral externo","La pelvis renal","El uréter distal"],c:1,e:"La vía urinaria termina en el meato uretral externo."},
 {id:28,cat:"via",q:"Los puntos pieloureterales (superior, medio e inferior) sirven para explorar:",o:["El hígado","El trayecto del uréter","El bazo","El páncreas"],c:1,e:"Son proyecciones en la pared abdominal para explorar el dolor a lo largo del uréter."},
 {id:29,cat:"via",q:"La puñopercusión positiva en el ángulo costovertebral orienta a compromiso:",o:["Hepático","Renal (p. ej. pielonefritis o litiasis)","Esplénico","Gástrico"],c:1,e:"El dolor a la puñopercusión en el ángulo costovertebral (maniobra de Giordano) sugiere patología renal."},
 {id:30,cat:"caso",q:"Juan Pérez presenta oliguria, creatinina 4.3 mg/dL y BUN 102: el cuadro es compatible con:",o:["Infección urinaria baja","Falla renal aguda","Cálculo vesical","Hipertrofia prostática benigna aislada"],c:1,e:"La caída aguda de la función renal con retención de creatinina/BUN y oliguria define la falla renal aguda."},
 {id:31,cat:"caso",q:"En la ecografía, riñones de tamaño normal con mala diferenciación corticomedular y sin dilatación sugieren daño:",o:["Obstructivo (posrenal)","Parenquimatoso agudo (no obstructivo)","Crónico terminal","Vascular por trombosis de vena porta"],c:1,e:"La ausencia de dilatación descarta obstrucción; la mala diferenciación corticomedular indica daño del parénquima."},
 {id:32,cat:"caso",q:"Que los riñones tengan tamaño NORMAL (no reducido) apoya que la falla es:",o:["Crónica avanzada","Aguda","Congénita","Poliquística"],c:1,e:"En la falla renal crónica avanzada los riñones suelen estar pequeños; el tamaño normal apoya un proceso agudo."},
 {id:33,cat:"caso",q:"Las arteriolas “en capa de cebolla” con necrosis fibrinoide en la biopsia corresponden a:",o:["Glomerulonefritis postinfecciosa","Nefropatía hipertensiva maligna","Riñón poliquístico","Necrosis tubular por contraste"],c:1,e:"El engrosamiento concéntrico “en capa de cebolla” y la necrosis fibrinoide arteriolar son típicos de la nefropatía hipertensiva maligna."},
 {id:34,cat:"caso",q:"En la hipertensión maligna, el daño renal se produce principalmente por lesión de:",o:["Los túbulos colectores","Las arteriolas (isquemia glomerular)","La cápsula renal","La pelvis renal"],c:1,e:"La HTA maligna lesiona las arteriolas; la isquemia glomerular resultante reduce la filtración."},
 {id:35,cat:"caso",q:"El potasio de 5.2 mEq/L del caso corresponde a:",o:["Hipopotasemia","Hiperpotasemia","Valor normal-bajo","Hipernatremia"],c:1,e:"5.2 mEq/L es hiperpotasemia leve, esperable al caer la filtración y la excreción renal de potasio."},
 {id:36,cat:"caso",q:"La oliguria del paciente (<110 cc/día) refleja una caída de:",o:["La reabsorción de sodio","La tasa de filtración glomerular (TFG)","La secreción de renina","La producción de eritropoyetina"],c:1,e:"La oliguria traduce una marcada disminución de la TFG por el daño glomerular/arteriolar."}
];'''
h=re.sub(r"const POOL=\[.*?\n\];", POOL, h, count=1, flags=re.S)

open(OUT,"w",encoding="utf-8").write(h)
print("renal.html escrito ·", len(h), "bytes")
print("juego restante:", h.count("🎮 Juego")+h.count("juego_respiratorio"))
print("preguntas:", h.count('cat:"'))
