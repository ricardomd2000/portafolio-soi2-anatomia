# -*- coding: utf-8 -*-
import re
SRC="/sessions/jolly-practical-gauss/mnt/corazon/practica_corazon/public/respiratorio.html"
OUT="/sessions/jolly-practical-gauss/mnt/corazon/practica_corazon/public/cerebro.html"
h=open(SRC,encoding="utf-8").read()

h=h.replace("<title>Vía Respiratoria Baja y Tórax · SOI II · Semana 2</title>","<title>Cerebro · SOI II · Semana 5</title>")
h=h.replace(
""":root{
  --rojo:#0f7391; --rojo-osc:#0a4f66; --rojo-cl:#3aa0bd;
  --azul:#155e75; --crema:#f4f9fb; --tinta:#20313a; --gris:#5c6b72;
  --verde:#2e7d5b; --ambar:#c77d0a; --linea:#d9e6ea;
  --sombra:0 4px 18px rgba(15,80,102,.10);
}""",
""":root{
  --rojo:#c2185b; --rojo-osc:#880e4f; --rojo-cl:#e91e63;
  --azul:#6a1b9a; --crema:#fdf4f8; --tinta:#20313a; --gris:#5c6b72;
  --verde:#2e7d5b; --ambar:#c77d0a; --linea:#f0dce6;
  --sombra:0 4px 18px rgba(136,14,79,.10);
}""")
h=h.replace("<h2>🫁 Vía Respiratoria Baja y Tórax</h2>","<h2>🧠 Cerebro: superficie, irrigación y venoso</h2>")
h=h.replace('<p class="mini" style="margin:0 0 6px">SOI II · Semana 2 — Identifícate para comenzar.</p>',
            '<p class="mini" style="margin:0 0 6px">SOI II · Semana 5 — Identifícate para comenzar.</p>')
h=h.replace("""  <h1>Tráquea, Bronquios, Pulmones y Pleura</h1>
  <p>Laboratorio de Anatomía · SOI II · Semana 2 · Integración con caso de tórax inestable</p>
  <p class="mini">Paredes del tórax y vía aérea inferior</p>""",
"""  <h1>Cerebro externo, irrigación y drenaje venoso</h1>
  <p>Laboratorio de Anatomía · SOI II · Semana 5 · Sistema Nervioso I · Integración con caso de ACV</p>
  <p class="mini">Lóbulos y surcos, círculo de Willis, meninges y senos venosos</p>""")

FASE1='''<!-- FASE 1 -->
<section class="fase prep activa" id="prep">
  <h2 class="sec">🧠 Antes de entrar al laboratorio</h2>
  <p class="intro">Llega dominando los lóbulos y surcos del cerebro, el círculo arterial de Willis con sus territorios, y las meninges con el drenaje venoso; así la correlación con el ACV te rendirá el doble.</p>

  <div class="card">
    <h3>Resultados de aprendizaje</h3>
    <ul class="limpia">
      <li>Identificar los surcos y circunvoluciones y relacionar cada lóbulo con su función general.</li>
      <li>Identificar el círculo arterial cerebral (Willis) y los territorios de las arterias cerebrales.</li>
      <li>Comprender las meninges, las divisiones de la duramadre y su relación con el drenaje venoso.</li>
      <li>Integrar la anatomía vascular con el caso de enfermedad cerebrovascular (ACV).</li>
    </ul>
  </div>

  <div class="card">
    <h3>Materiales para el laboratorio</h3>
    <ul class="limpia">
      <li>Modelos de encéfalo y cortes; preparaciones según disponibilidad.</li>
      <li>Atlas físico impreso y cuaderno para dibujar/rotular.</li>
      <li>Guantes, bata y EPP según norma del laboratorio.</li>
    </ul>
  </div>

  <div class="card">
    <h3>🎬 Videos de apoyo (Lecturio · requieren inicio de sesión institucional)</h3>
    <p class="mini">Ábrelos antes de venir. Se abren en una pestaña nueva con tu usuario de la biblioteca.</p>
    <div class="recursos" id="recursos"></div>
  </div>

  <div class="card">
    <h3>🎬 Videos complementarios (YouTube)</h3>
    <p class="mini">Toca cada tarjeta para reproducir. Refuerzan la anatomía del cerebro y su vascularización.</p>
    <div class="videos" id="vids-yt"></div>
  </div>

  <div class="card">
    <h3>Roles del equipo</h3>
    <ul class="limpia">
      <li><b>Líder:</b> administra el tiempo y el orden de las estaciones.</li>
      <li><b>Operador:</b> manipula modelos/preparaciones con cuidado.</li>
      <li><b>Relator clínico:</b> conecta hallazgos con el caso de ACV.</li>
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
    <span class="tag a">Estación A</span><span class="tag tiempo">Lóbulos y surcos</span>
    <h3>Superficie del hemisferio cerebral</h3>
    <div class="check" data-chk="A">
      <label><input type="checkbox"> Surco central (de Rolando): separa lóbulo frontal y parietal</label>
      <label><input type="checkbox"> Giro precentral (motor) y giro postcentral (sensitivo)</label>
      <label><input type="checkbox"> Surco lateral (de Silvio) y la ínsula en su profundidad</label>
      <label><input type="checkbox"> Surco parietooccipital: separa parietal y occipital</label>
      <label><input type="checkbox"> Lóbulos frontal, parietal, temporal y occipital</label>
      <label><input type="checkbox"> Surco longitudinal, cuerpo calloso, hoz del cerebro y tienda (tentorio) del cerebelo</label>
    </div>
    <div class="progreso"><i></i></div><div class="progtxt"></div>
    <div class="aviso">El giro <b>precentral</b> es la corteza motora primaria; el <b>postcentral</b>, la sensitiva primaria. Ambos representan el hemicuerpo contralateral.</div>
  </div>

  <div class="card">
    <span class="tag a">Estación B</span><span class="tag tiempo">Círculo de Willis</span>
    <h3>Polígono arterial de la base</h3>
    <div class="check" data-chk="B">
      <label><input type="checkbox"> Arterias carótidas internas (sistema carotídeo)</label>
      <label><input type="checkbox"> Arterias cerebrales anteriores (ACA) y comunicante anterior</label>
      <label><input type="checkbox"> Arterias comunicantes posteriores</label>
      <label><input type="checkbox"> Arterias cerebrales posteriores (ACP)</label>
      <label><input type="checkbox"> Arterias vertebrales que se unen en la arteria basilar</label>
      <label><input type="checkbox"> Cerebelosas: PICA (vertebral), AICA y SCA (basilar)</label>
    </div>
    <div class="progreso"><i></i></div><div class="progtxt"></div>
    <div class="nota">El círculo de Willis conecta el sistema <b>carotídeo</b> y el <b>vertebro-basilar</b>: da circulación colateral si se ocluye una arteria principal.</div>
  </div>

  <div class="card">
    <span class="tag a">Estación C</span><span class="tag tiempo">Territorios vasculares</span>
    <h3>Qué irriga cada arteria cerebral</h3>
    <div class="check" data-chk="C">
      <label><input type="checkbox"> ACA: cara medial (frontal/parietal) → pierna contralateral</label>
      <label><input type="checkbox"> ACM: cara lateral (motor/sensitivo de cara y brazo, lenguaje si es dominante)</label>
      <label><input type="checkbox"> ACP: lóbulo occipital → visión</label>
      <label><input type="checkbox"> Relación territorio ↔ déficit clínico</label>
    </div>
    <div class="progreso"><i></i></div><div class="progtxt"></div>
    <div class="aviso">Debilidad de <b>pierna</b> → ACA. Déficit de <b>cara/brazo</b> (± afasia) → ACM. <b>Hemianopsia</b> → ACP.</div>
  </div>

  <div class="card">
    <span class="tag a">Estación D</span><span class="tag tiempo">Meninges y drenaje venoso</span>
    <h3>Meninges, duramadre y senos</h3>
    <div class="check" data-chk="D">
      <label><input type="checkbox"> Meninges (de fuera a dentro): duramadre, aracnoides, piamadre</label>
      <label><input type="checkbox"> Espacio subaracnoideo (circula el LCR)</label>
      <label><input type="checkbox"> Pliegues de duramadre: hoz del cerebro y tienda del cerebelo</label>
      <label><input type="checkbox"> Senos venosos durales: sagital superior y seno recto</label>
      <label><input type="checkbox"> Confluencia de los senos (prensa de Herófilo)</label>
      <label><input type="checkbox"> Drenaje final hacia las venas yugulares internas</label>
    </div>
    <div class="progreso"><i></i></div><div class="progtxt"></div>
    <div class="nota">Los senos venosos durales corren <b>entre las dos capas de la duramadre</b> y drenan finalmente en las yugulares internas.</div>
  </div>
</section>

<!-- FASE 3 -->'''
h=re.sub(r"<!-- FASE 2 -->.*?<!-- FASE 3 -->", lambda m: FASE2, h, count=1, flags=re.S)

# quitar juego y agregar caso ACV antes del banco
h=re.sub(r'<div class="card">\s*<h3 style="margin-top:0">🎮 Juego.*?</div>\s*<h3>📝 Banco de preguntas</h3>', '<h3>📝 Banco de preguntas</h3>', h, count=1, flags=re.S)
h=h.replace('<h3>📝 Banco de preguntas</h3>',
'''<div class="card">
    <h3 style="margin-top:0">🔗 Integración con el caso (ACV)</h3>
    <p><b>Caso:</b> paciente con déficit neurológico <b>focal y súbito</b> por oclusión de una arteria cerebral (ACV isquémico). La clínica depende del <b>territorio</b> comprometido.</p>
    <div class="flujo"><span>Oclusión arterial</span><span class="fl">→</span><span>Isquemia del territorio</span><span class="fl">→</span><span>Déficit contralateral</span><span class="fl">→</span><span>ACM: cara/brazo + afasia · ACA: pierna · ACP: visión</span></div>
    <div class="nota"><b>Correlación:</b> el <b>círculo de Willis</b> puede ofrecer circulación colateral; el <b>giro precentral</b> del territorio afectado explica la debilidad contralateral. Un ACV por sangrado es <b>hemorrágico</b>.</div>
  </div>

  <h3>📝 Banco de preguntas</h3>''', 1)

h=h.replace(
"""    <ul class="limpia">
      <li>Una estructura que hoy dejé de confundir: __________</li>
      <li>En el caso, la dificultad respiratoria la conecto anatómicamente con: __________</li>
      <li>Dónde se acumularía sangre/líquido en el tórax de este paciente: __________</li>
    </ul>""",
"""    <ul class="limpia">
      <li>Una estructura que hoy dejé de confundir: __________</li>
      <li>El territorio de la arteria cerebral media incluye: __________</li>
      <li>Si el paciente tiene debilidad en la pierna, sospecho oclusión de: __________</li>
    </ul>""")

h=h.replace("<footer>Recurso de estudio · Vía respiratoria baja y tórax · SOI II Semana 2 · Uso educativo.</footer>",
            "<footer>Recurso de estudio · Cerebro externo, irrigación y drenaje venoso · SOI II Semana 5 · Uso educativo.</footer>")

h=h.replace("import { SUPABASE_URL, SUPABASE_KEY, TABLA_RESP, DOMINIO_INSTITUCIONAL } from './supabase-config.js';",
            "import { SUPABASE_URL, SUPABASE_KEY, TABLA_S5, DOMINIO_INSTITUCIONAL } from './supabase-config.js';")
h=h.replace("const TABLA=TABLA_RESP;","const TABLA=TABLA_S5;")

h=re.sub(r"const RECURSOS=\[.*?\];", '''const RECURSOS=[
  {id:"snc_curso1",t:"Sistema nervioso · encéfalo (Lecturio)",url:"https://unisabana.lecturio.com/#/course/c/7812/7602/7164"},
  {id:"snc_curso2",t:"Meninges y vascularización (Lecturio)",url:"https://unisabana.lecturio.com/#/course/c/7812/7602/7166"}
];''', h, count=1, flags=re.S)

h=re.sub(r"const YT=\[.*?\];", '''const YT=[
  {id:"3OqSyK05TtY",t:"Cerebro · lóbulos y surcos"},
  {id:"802xG1ysVL0",t:"Vascularización cerebral"},
  {id:"sSwPwSzAP_g",t:"Círculo de Willis"},
  {id:"wJkrVCClE8M",t:"Meninges"},
  {id:"0KkDYnoSPTA",t:"Drenaje venoso / senos"},
  {id:"1_r0y3P6TrY",t:"Complemento cerebro"}
];''', h, count=1, flags=re.S)

h=h.replace("const TEMAS_LABEL={torax:'Pared torácica',via:'Vía aérea',pulmon:'Pulmón y pleura',caso:'Caso clínico'};",
            "const TEMAS_LABEL={lobulos:'Lóbulos y surcos',willis:'Círculo de Willis',territorios:'Territorios vasculares',meninges:'Meninges y venoso',caso:'Caso: ACV'};")
h=h.replace("const catLbl={torax:'🦴 Pared torácica',via:'🫁 Vía aérea',pulmon:'🫁 Pulmón y pleura',caso:'🩺 Caso clínico'}[p.cat];",
            "const catLbl={lobulos:'🧠 Lóbulos y surcos',willis:'🩸 Círculo de Willis',territorios:'🗺️ Territorios',meninges:'🧫 Meninges y venoso',caso:'🩺 Caso: ACV'}[p.cat];")

POOL='''const POOL=[
 {id:1,cat:"lobulos",q:"El surco que separa el lóbulo frontal del parietal es el:",o:["Surco lateral","Surco central (de Rolando)","Surco parietooccipital","Surco calcarino"],c:1,e:"El surco central (de Rolando) separa el lóbulo frontal del parietal y limita las cortezas motora y sensitiva."},
 {id:2,cat:"lobulos",q:"El giro PREcentral corresponde a la corteza:",o:["Sensitiva primaria","Motora primaria","Visual","Auditiva"],c:1,e:"El giro precentral (delante del surco central) es la corteza motora primaria; controla el hemicuerpo contralateral."},
 {id:3,cat:"lobulos",q:"El giro POSTcentral corresponde a la corteza:",o:["Motora primaria","Sensitiva (somatosensorial) primaria","Visual","Del lenguaje"],c:1,e:"El giro postcentral es la corteza sensitiva general primaria."},
 {id:4,cat:"lobulos",q:"En la profundidad del surco lateral (de Silvio) se encuentra:",o:["El cuerpo calloso","La ínsula","El tálamo","El cerebelo"],c:1,e:"La ínsula queda oculta en el fondo del surco lateral; solo se ve separando sus bordes."},
 {id:5,cat:"lobulos",q:"El surco parietooccipital separa:",o:["Frontal y parietal","Parietal y occipital","Temporal y occipital","Los dos hemisferios"],c:1,e:"El surco parietooccipital separa el lóbulo parietal del occipital."},
 {id:6,cat:"lobulos",q:"El procesamiento visual primario ocurre en el lóbulo:",o:["Frontal","Temporal","Occipital","Parietal"],c:2,e:"El lóbulo occipital contiene la corteza visual primaria."},
 {id:7,cat:"lobulos",q:"Los dos hemisferios cerebrales están separados por:",o:["El surco central","El surco longitudinal (interhemisférico)","El surco lateral","La cisura calcarina"],c:1,e:"El surco longitudinal cerebral separa ambos hemisferios; aloja la hoz del cerebro y las arterias cerebrales anteriores."},
 {id:8,cat:"lobulos",q:"La gran comisura que conecta ambos hemisferios es:",o:["El fórnix","El cuerpo calloso","La comisura anterior","El tálamo"],c:1,e:"El cuerpo calloso es la mayor comisura interhemisférica."},
 {id:9,cat:"lobulos",q:"El pliegue de duramadre en forma de hoz entre los hemisferios es:",o:["La tienda del cerebelo","La hoz del cerebro","El diafragma selar","La hoz del cerebelo"],c:1,e:"La hoz del cerebro es el pliegue sagital de duramadre en el surco longitudinal."},
 {id:10,cat:"lobulos",q:"El pliegue de duramadre que separa el cerebro del cerebelo es:",o:["La hoz del cerebro","La tienda (tentorio) del cerebelo","El diafragma selar","La aracnoides"],c:1,e:"La tienda (tentorio) del cerebelo separa los lóbulos occipitales del cerebelo."},
 {id:11,cat:"willis",q:"El polígono de Willis conecta:",o:["Las dos yugulares","El sistema carotídeo y el vertebro-basilar","Las venas cerebrales","La aorta y la carótida externa"],c:1,e:"El círculo de Willis interconecta el sistema carotídeo interno y el vertebro-basilar, dando circulación colateral."},
 {id:12,cat:"willis",q:"La arteria comunicante anterior une:",o:["Las dos arterias cerebrales anteriores","Las cerebrales posteriores","La carótida con la basilar","Las vertebrales"],c:0,e:"La comunicante anterior conecta las dos ACA por delante."},
 {id:13,cat:"willis",q:"Las arterias comunicantes posteriores conectan:",o:["Las dos ACA","La carótida interna con la cerebral posterior","Las dos vertebrales","La basilar con la ACM"],c:1,e:"Las comunicantes posteriores unen el sistema carotídeo (carótida interna) con la cerebral posterior."},
 {id:14,cat:"willis",q:"Las arterias vertebrales se unen para formar:",o:["La arteria basilar","La carótida interna","La cerebral media","La comunicante posterior"],c:0,e:"Ambas arterias vertebrales confluyen en la arteria basilar."},
 {id:15,cat:"willis",q:"La arteria carótida interna se origina de:",o:["La aorta directamente","La carótida común","La subclavia","La basilar"],c:1,e:"La carótida interna nace de la bifurcación de la carótida común."},
 {id:16,cat:"willis",q:"La arteria cerebral posterior (ACP) pertenece al sistema:",o:["Carotídeo","Vertebro-basilar","Venoso","Meníngeo"],c:1,e:"La ACP es rama terminal de la basilar (sistema vertebro-basilar)."},
 {id:17,cat:"willis",q:"La arteria cerebelosa posteroinferior (PICA) se origina de:",o:["La arteria basilar","La arteria vertebral","La carótida interna","La ACM"],c:1,e:"La PICA nace de la arteria vertebral e irriga la parte inferior del cerebelo."},
 {id:18,cat:"willis",q:"La AICA y la SCA se originan de:",o:["Las vertebrales","La arteria basilar","La carótida interna","La comunicante posterior"],c:1,e:"La cerebelosa anteroinferior (AICA) y la superior (SCA) nacen de la basilar."},
 {id:19,cat:"territorios",q:"La arteria cerebral ANTERIOR (ACA) irriga principalmente:",o:["La cara lateral del hemisferio","La cara medial (frontal y parietal)","El lóbulo occipital","El cerebelo"],c:1,e:"La ACA irriga la superficie medial; su infarto afecta la pierna y el pie contralaterales."},
 {id:20,cat:"territorios",q:"La arteria cerebral MEDIA (ACM) irriga:",o:["La cara medial","La superficie lateral (áreas de cara y brazo, y lenguaje si es dominante)","El occipital","El tronco encefálico"],c:1,e:"La ACM irriga la cara lateral del hemisferio: motor/sensitivo de cara y brazo, y áreas del lenguaje en el hemisferio dominante."},
 {id:21,cat:"territorios",q:"La arteria cerebral POSTERIOR (ACP) irriga:",o:["El lóbulo frontal","El lóbulo occipital (visión)","La ínsula","La corteza motora"],c:1,e:"La ACP irriga el lóbulo occipital; su lesión produce déficit visual (hemianopsia)."},
 {id:22,cat:"territorios",q:"Una debilidad predominante en la PIERNA contralateral sugiere infarto de:",o:["ACM","ACA","ACP","PICA"],c:1,e:"El homúnculo de la pierna está en la cara medial (territorio de la ACA)."},
 {id:23,cat:"territorios",q:"Hemiparesia y afasia (déficit de cara/brazo y lenguaje) sugieren infarto de:",o:["ACP","ACM del hemisferio dominante","ACA","Cerebelosa"],c:1,e:"La ACM irriga áreas faciobraquiales y del lenguaje; su infarto en el hemisferio dominante da hemiparesia + afasia."},
 {id:24,cat:"territorios",q:"Una hemianopsia (pérdida de campo visual) orienta a compromiso de:",o:["ACA","ACM","ACP (occipital)","Basilar pontina"],c:2,e:"La corteza visual occipital depende de la ACP; su lesión causa déficit del campo visual."},
 {id:25,cat:"meninges",q:"El orden de las meninges de superficial a profunda es:",o:["Piamadre, aracnoides, duramadre","Duramadre, aracnoides, piamadre","Aracnoides, duramadre, piamadre","Duramadre, piamadre, aracnoides"],c:1,e:"De fuera a dentro: duramadre, aracnoides y piamadre."},
 {id:26,cat:"meninges",q:"El líquido cefalorraquídeo (LCR) circula en el espacio:",o:["Epidural","Subdural","Subaracnoideo","Extradural"],c:2,e:"El LCR ocupa el espacio subaracnoideo, entre aracnoides y piamadre."},
 {id:27,cat:"meninges",q:"Los senos venosos durales se localizan:",o:["En el espacio subaracnoideo","Entre las dos capas de la duramadre","Dentro del cerebro","Bajo la piamadre"],c:1,e:"Los senos durales corren entre las capas perióstica y meníngea de la duramadre."},
 {id:28,cat:"meninges",q:"El seno sagital superior recorre el borde de:",o:["La tienda del cerebelo","La hoz del cerebro","El diafragma selar","La aracnoides"],c:1,e:"El seno sagital superior discurre por el borde superior de la hoz del cerebro."},
 {id:29,cat:"meninges",q:"La confluencia de los senos venosos se denomina:",o:["Seno cavernoso","Prensa de Herófilo (confluencia de senos)","Golfo de la yugular","Seno recto"],c:1,e:"El seno sagital superior y el recto confluyen en la prensa de Herófilo."},
 {id:30,cat:"meninges",q:"El drenaje venoso del encéfalo termina finalmente en:",o:["Las venas yugulares internas","La vena cava superior directamente","La arteria basilar","El seno maxilar"],c:0,e:"Los senos durales drenan en las venas yugulares internas."},
 {id:31,cat:"caso",q:"Un déficit neurológico focal de inicio SÚBITO por oclusión arterial corresponde a:",o:["ACV isquémico","Migraña","Epilepsia","Tumor de crecimiento lento"],c:0,e:"El ACV isquémico produce un déficit focal súbito por interrupción del flujo en un territorio arterial."},
 {id:32,cat:"caso",q:"Un paciente con hemiparesia derecha y afasia probablemente tiene compromiso de:",o:["ACP derecha","ACM izquierda","ACA derecha","Cerebelosa"],c:1,e:"El lenguaje suele estar en el hemisferio izquierdo; la ACM izquierda explica hemiparesia derecha + afasia."},
 {id:33,cat:"caso",q:"La utilidad del círculo de Willis ante una oclusión es:",o:["Aumentar la presión","Ofrecer circulación colateral","Drenar el LCR","Producir mielina"],c:1,e:"Las anastomosis del polígono de Willis permiten flujo colateral cuando se ocluye una arteria principal."},
 {id:34,cat:"caso",q:"Un ACV producido por sangrado (rotura vascular) se denomina:",o:["Isquémico","Hemorrágico","Embólico","Lacunar"],c:1,e:"El ACV hemorrágico se debe a rotura de un vaso con sangrado intracraneal, a diferencia del isquémico."}
];'''
h=re.sub(r"const POOL=\[.*?\n\];", POOL, h, count=1, flags=re.S)

open(OUT,"w",encoding="utf-8").write(h)
print("cerebro.html", len(h), "bytes · preguntas:", h.count('cat:"'), "· juego:", h.count("🎮 Juego"))
