# -*- coding: utf-8 -*-
import re
SRC="/sessions/jolly-practical-gauss/mnt/corazon/practica_corazon/public/respiratorio.html"
OUT="/sessions/jolly-practical-gauss/mnt/corazon/SOI III/public/sentidos.html"
h=open(SRC,encoding="utf-8").read()

h=h.replace("<title>Vía Respiratoria Baja y Tórax · SOI II · Semana 2</title>","<title>Órganos de los sentidos · Ojo y Oído · SOI III</title>")
h=h.replace(
""":root{
  --rojo:#0f7391; --rojo-osc:#0a4f66; --rojo-cl:#3aa0bd;
  --azul:#155e75; --crema:#f4f9fb; --tinta:#20313a; --gris:#5c6b72;
  --verde:#2e7d5b; --ambar:#c77d0a; --linea:#d9e6ea;
  --sombra:0 4px 18px rgba(15,80,102,.10);
}""",
""":root{
  --rojo:#00838f; --rojo-osc:#005662; --rojo-cl:#4fb3bf;
  --azul:#00695c; --crema:#f2fafb; --tinta:#20313a; --gris:#5c6b72;
  --verde:#2e7d5b; --ambar:#c77d0a; --linea:#d3eaed;
  --sombra:0 4px 18px rgba(0,86,98,.10);
}""")
h=h.replace("<h2>🫁 Vía Respiratoria Baja y Tórax</h2>","<h2>👁️👂 Órganos de los sentidos · Ojo y Oído</h2>")
h=h.replace('<p class="mini" style="margin:0 0 6px">SOI II · Semana 2 — Identifícate para comenzar.</p>',
            '<p class="mini" style="margin:0 0 6px">SOI III — Identifícate para comenzar.</p>')
h=h.replace("""  <h1>Tráquea, Bronquios, Pulmones y Pleura</h1>
  <p>Laboratorio de Anatomía · SOI II · Semana 2 · Integración con caso de tórax inestable</p>
  <p class="mini">Paredes del tórax y vía aérea inferior</p>""",
"""  <h1>Anatomía del Ojo y del Oído</h1>
  <p>Laboratorio de Anatomía · SOI III · Órganos de los sentidos</p>
  <p class="mini">Órbita, globo ocular y anexos · oído externo, medio e interno</p>""")

FASE1='''<!-- FASE 1 -->
<section class="fase prep activa" id="prep">
  <h2 class="sec">🧠 Antes de entrar al laboratorio</h2>
  <p class="intro">Llega dominando la órbita y el globo ocular con sus capas, los músculos extraoculares y el sistema lacrimal, y las tres divisiones del oído; así la identificación te rendirá el doble.</p>

  <div class="card">
    <h3>Resultados de aprendizaje</h3>
    <ul class="limpia">
      <li>Describir la órbita, el globo ocular (capas y cámaras), los músculos extraoculares, el sistema lacrimal y la vascularización e inervación ocular.</li>
      <li>Explicar la anatomía del oído en sus tres divisiones (externo, medio e interno).</li>
      <li>Relacionar las estructuras con la visión, la audición y el equilibrio.</li>
    </ul>
  </div>

  <div class="card">
    <h3>Materiales para el laboratorio</h3>
    <ul class="limpia">
      <li>Modelos del ojo, la órbita y el oído; cráneo para huesos orbitarios y peñasco temporal.</li>
      <li>Atlas físico impreso y cuaderno para dibujar/rotular.</li>
      <li>Guantes, bata y EPP según norma del laboratorio.</li>
    </ul>
  </div>

  <div class="card">
    <h3>🎬 Recursos (Lecturio · requieren inicio de sesión institucional)</h3>
    <p class="mini">Ábrelos antes de venir. Se abren en una pestaña nueva con tu usuario de la biblioteca.</p>
    <div class="recursos" id="recursos"></div>
  </div>

  <div class="card">
    <h3>🎬 Videos complementarios (YouTube)</h3>
    <p class="mini">Toca cada tarjeta para reproducir. Refuerzan la anatomía del ojo y del oído.</p>
    <div class="videos" id="vids-yt"></div>
  </div>

  <div class="card">
    <h3>Roles del equipo</h3>
    <ul class="limpia">
      <li><b>Líder:</b> administra el tiempo y el orden de las estaciones.</li>
      <li><b>Operador:</b> manipula modelos con cuidado.</li>
      <li><b>Relator clínico:</b> conecta hallazgos con la clínica (otitis, glaucoma, vértigo…).</li>
      <li><b>Auditor:</b> diligencia los checklists y controla la calidad.</li>
    </ul>
  </div>
</section>

<!-- FASE 2 -->'''
h=re.sub(r"<!-- FASE 1 -->.*?<!-- FASE 2 -->", lambda m: FASE1, h, count=1, flags=re.S)

FASE2='''<!-- FASE 2 -->
<section class="fase dur" id="dur">
  <h2 class="sec">🔬 Durante la práctica</h2>
  <p class="intro">Trabaja estación por estación. Marca cada estructura al identificarla con seguridad.</p>

  <div class="card">
    <span class="tag a">Estación A</span><span class="tag tiempo">Órbita</span>
    <h3>Paredes y aberturas orbitarias</h3>
    <div class="check" data-chk="A">
      <label><input type="checkbox"> 7 huesos: frontal, esfenoides, cigomático, maxilar, palatino, etmoides, lacrimal</label>
      <label><input type="checkbox"> Techo (frontal) y piso (maxilar)</label>
      <label><input type="checkbox"> Pared medial (etmoides/lacrimal) y lateral (cigomático + ala mayor del esfenoides)</label>
      <label><input type="checkbox"> Agujero/canal óptico: nervio óptico y arteria oftálmica</label>
      <label><input type="checkbox"> Fisura orbitaria superior: III, IV, V1 y VI</label>
      <label><input type="checkbox"> Fisura orbitaria inferior: nervio maxilar (V2)</label>
    </div>
    <div class="progreso"><i></i></div><div class="progtxt"></div>
    <div class="aviso">Por el <b>canal óptico</b> pasan el nervio óptico y la arteria oftálmica; por la <b>fisura orbitaria superior</b>, los nervios de la motilidad ocular (III, IV, VI) y V1.</div>
  </div>

  <div class="card">
    <span class="tag a">Estación B</span><span class="tag tiempo">Globo ocular</span>
    <h3>Las tres capas (túnicas)</h3>
    <div class="check" data-chk="B">
      <label><input type="checkbox"> Túnica fibrosa: córnea (1/6 anterior) y esclerótica; limbo esclerocorneal</label>
      <label><input type="checkbox"> Túnica vascular (úvea): coroides, cuerpo ciliar e iris</label>
      <label><input type="checkbox"> Cuerpo ciliar: músculo ciliar (acomodación) y producción de humor acuoso</label>
      <label><input type="checkbox"> Túnica nerviosa: retina (conos y bastones)</label>
      <label><input type="checkbox"> Mácula y fóvea (máxima agudeza) · disco óptico · ora serrata</label>
    </div>
    <div class="progreso"><i></i></div><div class="progtxt"></div>
    <div class="nota">La <b>córnea</b> es transparente y avascular (principal medio de refracción); la <b>fóvea</b> concentra conos y da la mayor agudeza visual.</div>
  </div>

  <div class="card">
    <span class="tag a">Estación C</span><span class="tag tiempo">Músculos y anexos</span>
    <h3>Motilidad, lágrima e irrigación</h3>
    <div class="check" data-chk="C">
      <label><input type="checkbox"> 4 rectos (superior, inferior, medial, lateral) desde el anillo de Zinn</label>
      <label><input type="checkbox"> 2 oblicuos (superior con tróclea, inferior)</label>
      <label><input type="checkbox"> Sistema lacrimal: glándula → puntos → canalículos → saco → conducto nasolacrimal</label>
      <label><input type="checkbox"> Párpados, tarsos y glándulas de Meibomio; conjuntiva (palpebral y bulbar)</label>
      <label><input type="checkbox"> Arteria oftálmica (rama de la carótida interna) y arteria central de la retina</label>
    </div>
    <div class="progreso"><i></i></div><div class="progtxt"></div>
    <div class="aviso">El recto lateral <b>abduce</b> (VI), el medial <b>aduce</b>; el oblicuo superior pasa por la <b>tróclea</b> (IV). La irrigación depende de la <b>arteria oftálmica</b>.</div>
  </div>

  <div class="card">
    <span class="tag a">Estación D</span><span class="tag tiempo">Oído externo y medio</span>
    <h3>Del pabellón a los osículos</h3>
    <div class="check" data-chk="D">
      <label><input type="checkbox"> Pabellón: hélix, antihélix, trago, antitrago, concha y lóbulo</label>
      <label><input type="checkbox"> Conducto auditivo externo (S) y glándulas ceruminosas</label>
      <label><input type="checkbox"> Membrana timpánica: pars tensa/flácida, umbo y cono luminoso</label>
      <label><input type="checkbox"> Osículos: martillo, yunque y estribo (base en la ventana oval)</label>
      <label><input type="checkbox"> Músculos: tensor del tímpano y estapedio (reflejo estapedial)</label>
      <label><input type="checkbox"> Trompa de Eustaquio (tuba auditiva) hacia la nasofaringe</label>
    </div>
    <div class="progreso"><i></i></div><div class="progtxt"></div>
    <div class="nota">La cadena de osículos amplifica el sonido de la membrana timpánica a la <b>ventana oval</b>; la <b>trompa de Eustaquio</b> iguala la presión del oído medio.</div>
  </div>

  <div class="card">
    <span class="tag a">Estación E</span><span class="tag tiempo">Oído interno</span>
    <h3>Laberinto: audición y equilibrio</h3>
    <div class="check" data-chk="E">
      <label><input type="checkbox"> Laberinto óseo y membranoso (perilinfa / endolinfa)</label>
      <label><input type="checkbox"> Cóclea: rampas vestibular, media y timpánica</label>
      <label><input type="checkbox"> Órgano de Corti (membrana basilar) con células ciliadas → audición</label>
      <label><input type="checkbox"> 3 canales semicirculares (aceleración angular)</label>
      <label><input type="checkbox"> Utrículo y sáculo (aceleración lineal / gravedad)</label>
      <label><input type="checkbox"> Nervio vestibulococlear (VIII par)</label>
    </div>
    <div class="progreso"><i></i></div><div class="progtxt"></div>
    <div class="aviso">La <b>cóclea</b> (órgano de Corti) es para la audición; los <b>canales semicirculares, utrículo y sáculo</b> para el equilibrio. Todo lo lleva el <b>VIII par</b>.</div>
  </div>
</section>

<!-- FASE 3 -->'''
h=re.sub(r"<!-- FASE 2 -->.*?<!-- FASE 3 -->", lambda m: FASE2, h, count=1, flags=re.S)

h=re.sub(r'<div class="card">\s*<h3 style="margin-top:0">🎮 Juego.*?<h3>📝 Banco de preguntas</h3>', '<h3>📝 Banco de preguntas</h3>', h, count=1, flags=re.S)

h=h.replace(
"""    <ul class="limpia">
      <li>Una estructura que hoy dejé de confundir: __________</li>
      <li>En el caso, la dificultad respiratoria la conecto anatómicamente con: __________</li>
      <li>Dónde se acumularía sangre/líquido en el tórax de este paciente: __________</li>
    </ul>""",
"""    <ul class="limpia">
      <li>Una estructura que hoy dejé de confundir: __________</li>
      <li>Por el canal óptico pasan: __________</li>
      <li>La estructura del oído interno para la audición es: __________</li>
    </ul>""")

h=h.replace("<footer>Recurso de estudio · Vía respiratoria baja y tórax · SOI II Semana 2 · Uso educativo.</footer>",
            "<footer>Recurso de estudio · Órganos de los sentidos (ojo y oído) · SOI III · Uso educativo.</footer>")

h=h.replace("import { SUPABASE_URL, SUPABASE_KEY, TABLA_RESP, DOMINIO_INSTITUCIONAL } from './supabase-config.js';",
            "import { SUPABASE_URL, SUPABASE_KEY, TABLA_SENT, DOMINIO_INSTITUCIONAL } from './supabase-config.js';")
h=h.replace("const TABLA=TABLA_RESP;","const TABLA=TABLA_SENT;")
h=h.replace("sb.from('autorizados')","sb.from('autorizados_soi3')")

h=re.sub(r"const RECURSOS=\[.*?\];", '''const RECURSOS=[
  {id:"oido1",t:"Oído (Lecturio) 1",url:"https://unisabana.lecturio.com/#/lecture/s/83506/252951?return=/search/ear"},
  {id:"oido2",t:"Oído (Lecturio) 2",url:"https://unisabana.lecturio.com/#/lecture/s/83506/252952?return=/search/ear"},
  {id:"acland",t:"Ojo y oído (Acland, multimedia)",url:"https://es-aclandanatomy-com.ez.unisabana.edu.co/Multimedia.aspx?categoryid=40457"}
];''', h, count=1, flags=re.S)

h=re.sub(r"const YT=\[.*?\];", '''const YT=[
  {id:"2DeygrHiN6k",t:"Anatomía del ojo"},
  {id:"3TJ1cfi4pUg",t:"Órbita / globo ocular"},
  {id:"Wqev5bARcmQ",t:"Anatomía del oído"},
  {id:"gfsOuS-3F94",t:"Oído interno / audición"}
];''', h, count=1, flags=re.S)

h=h.replace("const TEMAS_LABEL={torax:'Pared torácica',via:'Vía aérea',pulmon:'Pulmón y pleura',caso:'Caso clínico'};",
            "const TEMAS_LABEL={orbita:'Órbita',globo:'Globo ocular',anexos:'Músculos y anexos',oidoext:'Oído externo/medio',oidoint:'Oído interno'};")
h=h.replace("const catLbl={torax:'🦴 Pared torácica',via:'🫁 Vía aérea',pulmon:'🫁 Pulmón y pleura',caso:'🩺 Caso clínico'}[p.cat];",
            "const catLbl={orbita:'🦴 Órbita',globo:'👁️ Globo ocular',anexos:'💧 Músculos y anexos',oidoext:'👂 Oído ext/medio',oidoint:'🌀 Oído interno'}[p.cat];")

POOL='''const POOL=[
 {id:1,cat:"orbita",q:"La órbita tiene forma de:",o:["Cubo","Pirámide cuadrangular (base anterior, vértice posterior)","Esfera","Cilindro"],c:1,e:"La órbita es una pirámide cuadrangular con base anterior y vértice posterior."},
 {id:2,cat:"orbita",q:"El TECHO de la órbita lo forma principalmente el hueso:",o:["Maxilar","Frontal","Cigomático","Etmoides"],c:1,e:"El hueso frontal forma el techo; el maxilar, gran parte del piso."},
 {id:3,cat:"orbita",q:"La pared MEDIAL de la órbita está formada sobre todo por:",o:["Cigomático","Etmoides y lacrimal","Maxilar","Esfenoides"],c:1,e:"La pared medial la forman el etmoides y el lacrimal (muy delgada)."},
 {id:4,cat:"orbita",q:"Por el canal/agujero óptico pasan:",o:["El nervio maxilar","El nervio óptico y la arteria oftálmica","El III par solamente","La vena oftálmica solamente"],c:1,e:"El canal óptico da paso al nervio óptico (II) y a la arteria oftálmica."},
 {id:5,cat:"orbita",q:"Por la fisura orbitaria SUPERIOR pasan los nervios:",o:["Óptico y maxilar","Oculomotor (III), troclear (IV), oftálmico (V1) y abducens (VI)","Facial y vestibulococlear","Solo el V2"],c:1,e:"La fisura orbitaria superior transmite el III, IV, V1 y VI."},
 {id:6,cat:"orbita",q:"El nervio maxilar (V2) pasa por la fisura orbitaria:",o:["Superior","Inferior","Media","Óptica"],c:1,e:"La fisura orbitaria inferior da paso al nervio maxilar (V2) y vasos infraorbitarios."},
 {id:7,cat:"orbita",q:"Cuántos huesos forman la órbita:",o:["Cuatro","Cinco","Siete","Nueve"],c:2,e:"Siete huesos: frontal, esfenoides, cigomático, maxilar, palatino, etmoides y lacrimal."},
 {id:8,cat:"globo",q:"La túnica FIBROSA del globo ocular está formada por:",o:["Coroides e iris","Córnea y esclerótica","Retina","Cuerpo ciliar"],c:1,e:"La túnica fibrosa externa está formada por la córnea (anterior) y la esclerótica (posterior)."},
 {id:9,cat:"globo",q:"El principal medio de refracción del ojo, transparente y avascular, es:",o:["El cristalino","La córnea","La esclerótica","La retina"],c:1,e:"La córnea, transparente y avascular, ocupa el sexto anterior y es el principal medio de refracción."},
 {id:10,cat:"globo",q:"La túnica vascular (úvea) está compuesta por:",o:["Córnea, esclerótica y limbo","Coroides, cuerpo ciliar e iris","Retina y nervio óptico","Cristalino y humor vítreo"],c:1,e:"La úvea = coroides + cuerpo ciliar + iris."},
 {id:11,cat:"globo",q:"El humor acuoso y la acomodación del cristalino dependen del:",o:["Iris","Cuerpo ciliar (músculo ciliar)","Disco óptico","Limbo"],c:1,e:"El cuerpo ciliar produce el humor acuoso y su músculo ciliar controla la acomodación."},
 {id:12,cat:"globo",q:"Los fotorreceptores (conos y bastones) están en:",o:["La coroides","La retina","La esclerótica","El iris"],c:1,e:"La retina (túnica nerviosa) contiene los conos y bastones."},
 {id:13,cat:"globo",q:"El área de MAYOR agudeza visual es:",o:["El disco óptico","La fóvea (en la mácula)","La ora serrata","El limbo"],c:1,e:"La fóvea, en la mácula, tiene la mayor concentración de conos y la máxima agudeza."},
 {id:14,cat:"globo",q:"El punto por donde salen las fibras y no hay fotorreceptores (punto ciego) es:",o:["La mácula","El disco óptico","La ora serrata","La pupila"],c:1,e:"El disco óptico es donde convergen las fibras para formar el nervio óptico; no tiene fotorreceptores."},
 {id:15,cat:"globo",q:"El iris regula:",o:["La forma de la córnea","El tamaño de la pupila (cantidad de luz)","La producción de lágrima","La presión venosa"],c:1,e:"El iris, con sus músculos, regula el diámetro pupilar y la entrada de luz."},
 {id:16,cat:"anexos",q:"Los músculos rectos del ojo se originan en:",o:["La tróclea","El anillo tendinoso común (de Zinn)","El tarso","El limbo"],c:1,e:"Los cuatro rectos nacen del anillo de Zinn en el vértice de la órbita."},
 {id:17,cat:"anexos",q:"El músculo que ABDUCE el ojo es el:",o:["Recto medial","Recto lateral","Oblicuo inferior","Recto superior"],c:1,e:"El recto lateral abduce (inervado por el VI); el recto medial aduce."},
 {id:18,cat:"anexos",q:"El músculo que pasa por una tróclea en el ángulo superomedial es el:",o:["Oblicuo inferior","Oblicuo superior","Recto superior","Elevador del párpado"],c:1,e:"El oblicuo superior pasa por la tróclea; lo inerva el nervio troclear (IV)."},
 {id:19,cat:"anexos",q:"La secuencia de drenaje de la lágrima es:",o:["Glándula → conducto nasolacrimal → puntos → saco","Puntos → canalículos → saco lacrimal → conducto nasolacrimal","Saco → puntos → glándula → nariz","Glándula → tróclea → nariz"],c:1,e:"La lágrima drena por los puntos → canalículos → saco lacrimal → conducto nasolacrimal → cavidad nasal."},
 {id:20,cat:"anexos",q:"Las glándulas de Meibomio (en los tarsos) producen:",o:["La capa acuosa","La capa lipídica de la película lacrimal","La capa mucosa","El humor acuoso"],c:1,e:"Las glándulas de Meibomio aportan la capa lipídica; la glándula lacrimal, la acuosa."},
 {id:21,cat:"anexos",q:"La irrigación del ojo depende sobre todo de la arteria:",o:["Facial","Oftálmica (rama de la carótida interna)","Maxilar","Temporal superficial"],c:1,e:"La arteria oftálmica, rama de la carótida interna, entra por el canal óptico e irriga el ojo."},
 {id:22,cat:"anexos",q:"La arteria que irriga específicamente la retina es la:",o:["Arteria central de la retina","Arteria facial","Arteria lagrimal","Vena oftálmica"],c:0,e:"La arteria central de la retina, rama de la oftálmica, irriga la retina."},
 {id:23,cat:"oidoext",q:"El borde más externo del pabellón auricular es:",o:["El trago","El hélix","La concha","El lóbulo"],c:1,e:"El hélix es el borde externo; el trago es la proyección frente al conducto."},
 {id:24,cat:"oidoext",q:"El conducto auditivo externo tiene, hacia dentro, una porción:",o:["Totalmente cartilaginosa","Ósea (2/3 internos) y cartilaginosa (1/3 externo)","Totalmente ósea","Membranosa"],c:1,e:"El tercio externo es cartilaginoso y los dos tercios internos, óseos."},
 {id:25,cat:"oidoext",q:"El vértice (umbo) de la membrana timpánica corresponde a la inserción de:",o:["El estribo","El mango del martillo","El yunque","La trompa de Eustaquio"],c:1,e:"El mango del martillo se adhiere a la membrana timpánica; su punto más deprimido es el umbo."},
 {id:26,cat:"oidoext",q:"Los tres osículos, en orden desde la membrana timpánica, son:",o:["Estribo, yunque, martillo","Martillo, yunque, estribo","Yunque, martillo, estribo","Martillo, estribo, yunque"],c:1,e:"Martillo → yunque → estribo; la base del estribo se articula con la ventana oval."},
 {id:27,cat:"oidoext",q:"La base del estribo se articula con:",o:["La ventana redonda","La ventana oval","La trompa de Eustaquio","El conducto coclear"],c:1,e:"La base (platina) del estribo ocupa la ventana oval, transmitiendo la vibración al oído interno."},
 {id:28,cat:"oidoext",q:"La trompa de Eustaquio conecta el oído medio con:",o:["La órbita","La nasofaringe","El seno maxilar","La mastoides"],c:1,e:"La tuba auditiva (Eustaquio) comunica el oído medio con la nasofaringe e iguala la presión."},
 {id:29,cat:"oidoext",q:"El reflejo estapedial (protección ante sonidos intensos) lo producen:",o:["Los canales semicirculares","El tensor del tímpano y el estapedio","La trompa de Eustaquio","El órgano de Corti"],c:1,e:"El tensor del tímpano y el estapedio se contraen ante sonidos fuertes, reduciendo la transmisión."},
 {id:30,cat:"oidoint",q:"El oído interno (laberinto) se aloja en el hueso:",o:["Frontal","Temporal (porción petrosa)","Occipital","Esfenoides"],c:1,e:"El laberinto está en la porción petrosa (peñasco) del hueso temporal."},
 {id:31,cat:"oidoint",q:"La estructura responsable de la AUDICIÓN es:",o:["Los canales semicirculares","La cóclea (órgano de Corti)","El utrículo","El sáculo"],c:1,e:"La cóclea, con el órgano de Corti, transforma la vibración en impulsos: es la audición."},
 {id:32,cat:"oidoint",q:"El líquido que contiene la rampa media (conducto coclear) es:",o:["Perilinfa","Endolinfa","Humor acuoso","Líquido cefalorraquídeo"],c:1,e:"La rampa media contiene endolinfa; las rampas vestibular y timpánica, perilinfa."},
 {id:33,cat:"oidoint",q:"Las células ciliadas de la audición están en:",o:["La mácula del utrículo","El órgano de Corti (sobre la membrana basilar)","Las crestas ampulares","El sáculo"],c:1,e:"El órgano de Corti, sobre la membrana basilar, aloja las células ciliadas auditivas."},
 {id:34,cat:"oidoint",q:"Los canales semicirculares detectan:",o:["La aceleración lineal","La aceleración angular (giros de la cabeza)","La luz","La presión"],c:1,e:"Los tres canales semicirculares detectan la aceleración angular en los tres planos."},
 {id:35,cat:"oidoint",q:"El utrículo y el sáculo detectan:",o:["El sonido","La aceleración lineal y la posición respecto a la gravedad","La aceleración angular","La temperatura"],c:1,e:"El utrículo y el sáculo (órganos otolíticos) detectan aceleración lineal y la gravedad."},
 {id:36,cat:"oidoint",q:"El nervio que lleva la audición y el equilibrio al tronco encefálico es el:",o:["Facial (VII)","Vestibulococlear (VIII)","Trigémino (V)","Glosofaríngeo (IX)"],c:1,e:"El VIII par (vestibulococlear) transmite la información auditiva y vestibular."}
];'''
h=re.sub(r"const POOL=\[.*?\n\];", POOL, h, count=1, flags=re.S)

# botón flotante de recursos
h=h.replace("</body>", '<a href="recursos.html" style="position:fixed;right:16px;bottom:16px;z-index:500;background:#0f7391;color:#fff;text-decoration:none;padding:11px 16px;border-radius:999px;font-weight:600;box-shadow:0 6px 18px rgba(0,0,0,.28);font-family:system-ui,sans-serif;font-size:.9rem">📚 Recursos</a>\n</body>')

open(OUT,"w",encoding="utf-8").write(h)
print("sentidos.html", len(h), "bytes · preguntas:", h.count('cat:"'), "· autorizados_soi3:", h.count("autorizados_soi3"), "· juego:", h.count("🎮 Juego"))
