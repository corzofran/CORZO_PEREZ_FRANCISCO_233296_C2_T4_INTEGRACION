"""Corpus sintético (parte A): agua, café y cacao, turismo, salud y riesgos naturales.

Los textos fueron REDACTADOS para este proyecto (no provienen de ninguna fuente externa). Los lugares son reales
(Chiapas, México), pero los sucesos descritos son ilustrativos. Cada entrada: (tema, subtema, titulo, texto).
"""

DOCS_A = [
    # ---------------------------------------------------------------- AGUA
    ("agua", "agua-colonias",
     "Colonias del norte de Tuxtla enfrentan desabasto de agua por segunda semana",
     "Cientos de familias de las colonias del norte de la capital chiapaneca llevan dos semanas sin recibir agua en sus "
     "tomas domiciliarias. Los vecinos aseguran que el líquido llega apenas unas horas al día y con muy poca presión, por "
     "lo que han tenido que comprar pipas a precios cada vez más altos para llenar tinacos y cisternas. El organismo "
     "operador explicó que la causa es una falla en una bomba del sistema de bombeo y que trabaja en su reparación, "
     "mientras reparte agua con camiones cisterna en los puntos más afectados. Habitantes piden un calendario de entrega "
     "claro y advierten que la escasez golpea sobre todo a adultos mayores y a negocios pequeños que dependen del "
     "abastecimiento diario."),
    ("agua", "agua-agro",
     "La sequía reduce la cosecha de maíz y frijol en la región Frailesca",
     "Productores de la región Frailesca reportan pérdidas importantes en sus parcelas de maíz y frijol debido a la falta "
     "de lluvias durante el periodo de siembra. Los campesinos explican que la humedad del suelo no fue suficiente para "
     "que las plantas completaran su desarrollo, y que muchas mazorcas salieron pequeñas o vacías. Técnicos agrícolas "
     "recomiendan sembrar variedades más resistentes a la sequía, aplicar cobertura vegetal para conservar la humedad y "
     "construir pequeñas obras de captación en las parcelas. Algunas familias ya consideran vender parte de su ganado "
     "para cubrir deudas, y piden apoyos para comprar semilla y fertilizante antes del próximo ciclo agrícola, pues "
     "temen que el temporal vuelva a retrasarse."),
    ("agua", "agua-presa",
     "Baja el nivel de las presas y preocupa la generación de energía hidroeléctrica",
     "El nivel de almacenamiento de las presas del río Grijalva descendió varios metros respecto al promedio de la "
     "temporada, lo que despierta preocupación entre ingenieros y autoridades. Un embalse con menos volumen significa "
     "menos capacidad para mover las turbinas de las hidroeléctricas y menos reserva para abastecer a los municipios "
     "cercanos. Especialistas señalan que el cambio en el patrón de lluvias y las altas temperaturas aceleran la "
     "evaporación. Por ello recomiendan administrar con cuidado las descargas, vigilar la calidad del agua almacenada y "
     "planear con anticipación los meses más secos. Mientras tanto, pescadores de las orillas ven cómo retroceden las "
     "aguas y cómo quedan expuestos tramos de lecho que antes permanecían cubiertos."),
    ("agua", "agua-potable",
     "Inauguran planta potabilizadora para mejorar la calidad del agua en cabeceras municipales",
     "Una nueva planta potabilizadora comenzó a operar para filtrar y clorar el agua que consumen miles de habitantes de "
     "la zona. El sistema retira sedimentos, reduce bacterias y mide de manera continua el cloro residual para asegurar "
     "que el líquido llegue seguro a las viviendas. Personal técnico explicó que antes del proyecto muchas familias "
     "hervían el agua o compraban garrafones, lo que representaba un gasto constante. Además, la instalación incluye un "
     "laboratorio donde se analizan muestras semanales de distintos puntos de la red. Las autoridades sanitarias pidieron "
     "a la población no desperdiciar el recurso, reportar fugas y mantener limpios los tinacos, pues una buena "
     "infraestructura no basta si el almacenamiento doméstico se contamina."),
    ("agua", "agua-lluvias",
     "Inicia la temporada de lluvias y especialistas llaman a recargar los acuíferos",
     "Con la llegada del temporal de lluvias, especialistas en hidrología recordaron que gran parte del agua que cae se "
     "pierde por escurrimiento si no existen zonas de infiltración. Proponen conservar bosques y áreas verdes, construir "
     "pozos de absorción y evitar que el cemento cubra todos los terrenos de las ciudades. Un acuífero bien recargado "
     "funciona como una reserva natural para los meses de estiaje, cuando los ríos bajan y las fuentes superficiales se "
     "agotan. También advirtieron que la sobreexplotación de pozos profundos puede abatir el nivel freático y encarecer "
     "la extracción. Invitaron a los municipios a vigilar las concesiones y a escuchar a las comunidades que han cuidado "
     "sus manantiales por generaciones."),
    ("agua", "agua-ahorro",
     "Campaña escolar enseña a ahorrar agua y a captar lluvia en casa",
     "Estudiantes de primaria y secundaria participan en una campaña que les enseña a cuidar el agua desde su hogar. Los "
     "talleres explican cómo reparar fugas en llaves e inodoros, cómo reutilizar el agua de la regadera para limpiar "
     "patios y cómo instalar canaletas sencillas para captar la lluvia de los techos. Los maestros organizaron concursos "
     "de dibujo y pequeñas maquetas de sistemas de recolección, con premios para los grupos más creativos. Madres y "
     "padres de familia se han sumado revisando el consumo en sus recibos y comparando resultados. Los organizadores "
     "esperan que los niños se conviertan en promotores del uso responsable del líquido, pues el ahorro cotidiano es más "
     "barato que construir nueva infraestructura."),
    # ---------------------------------------------------------------- CAFÉ Y CACAO
    ("cafe_cacao", "cafe-exportacion",
     "Cooperativas chiapanecas exportan café orgánico a Europa y Norteamérica",
     "Un grupo de cooperativas de la sierra chiapaneca concretó nuevos envíos de café orgánico de altura hacia mercados "
     "europeos y norteamericanos. Los productores destacan que el grano cuenta con certificaciones que garantizan que se "
     "cultiva sin agroquímicos y con prácticas de conservación del suelo. El proceso incluye cosecha manual de cerezas "
     "maduras, beneficiado húmedo, secado al sol y selección por tamaño y defectos antes de empacar en sacos de yute. "
     "Compradores internacionales valoran las notas a chocolate y frutos rojos de las muestras que probaron. Para los "
     "socios, la exportación representa mejores ingresos que la venta local, aunque reconocen que cumplir con los "
     "trámites aduanales y las auditorías exige tiempo, capacitación y una administración muy ordenada."),
    ("cafe_cacao", "cafe-roya",
     "La roya del café avanza en cafetales de altura y obliga a renovar plantas",
     "Productores de café reportan que la roya, un hongo que provoca manchas amarillas en las hojas, ha avanzado en "
     "varias fincas de altura. La enfermedad debilita los cafetos, reduce la fotosíntesis y puede provocar la caída de "
     "las hojas antes de que maduren los frutos. Técnicos recomiendan podar, mejorar la sombra, aplicar caldos minerales "
     "y sustituir las plantas viejas por variedades más tolerantes. También sugieren revisar los cafetales con "
     "frecuencia para detectar a tiempo los focos de infección. Algunos agricultores explican que la renovación cuesta "
     "mucho y tarda años en dar resultados, por lo que piden créditos blandos y viveros cercanos. Sin apoyo, advierten, "
     "muchas familias podrían abandonar el cultivo y emigrar."),
    ("cafe_cacao", "cacao-soconusco",
     "El cacao del Soconusco recupera presencia en el mercado gracias a nuevas plantaciones",
     "En la región del Soconusco, cerca de la frontera con Guatemala, productores de cacao reportan que las nuevas "
     "plantaciones comienzan a dar fruto después de varios años de espera. El cacao criollo de la zona se aprecia por su "
     "aroma floral y su baja amargura, cualidades que buscan los fabricantes de chocolate fino. Los agricultores "
     "aprendieron a injertar árboles productivos, a controlar la moniliasis y a fermentar las almendras en cajones de "
     "madera para mejorar el sabor. Aunque la cosecha sigue siendo pequeña comparada con la de otros países, los "
     "comercializadores aseguran que existe demanda para lotes de calidad. Los técnicos insisten en que el éxito depende "
     "de mantener la sombra, cuidar los suelos y vender con contratos justos."),
    ("cafe_cacao", "cacao-chocolate",
     "Chocolateros artesanales de San Cristóbal transforman el cacao local en barras y bebidas",
     "Pequeños talleres de chocolate artesanal en San Cristóbal de las Casas compran cacao de productores locales para "
     "tostarlo, molerlo y convertirlo en barras, bombones y bebidas calientes. Los maestros chocolateros explican que el "
     "proceso comienza con la selección de las almendras, continúa con el tostado a fuego lento y termina con el "
     "conchado, que suaviza la textura. Muchos negocios mezclan el cacao con canela, chile o azúcar de caña para elaborar "
     "recetas tradicionales. Los visitantes pueden asistir a talleres donde preparan su propia tableta y aprenden la "
     "historia de la bebida en la región. Los dueños señalan que pagar mejor al productor garantiza calidad constante, y "
     "que el turismo ayuda a darle un precio justo al producto."),
    ("cafe_cacao", "cafe-cooperativa",
     "Pequeños productores se organizan en cooperativa para vender café con comercio justo",
     "Familias cafetaleras de una comunidad indígena formaron una cooperativa para vender juntas su cosecha y negociar "
     "mejores precios con compradores de comercio justo. Antes dependían de intermediarios que pagaban poco y por "
     "adelantado, lo que dejaba a muchos productores endeudados. Ahora comparten un beneficio húmedo, un secadero y una "
     "bodega, y llevan registros de volumen y calidad por socio. La asamblea decide cómo usar el sobreprecio que reciben, "
     "y gran parte se destina a una escuela, una clínica y caminos. Los dirigentes cuentan que las mujeres participan "
     "cada vez más en las decisiones y en la administración. Aun así, reconocen que mantener la unión exige confianza, "
     "transparencia en las cuentas y paciencia."),
    ("cafe_cacao", "cafe-precios",
     "El precio internacional del café cae y preocupa a los productores de la sierra",
     "La baja en el precio internacional del café inquieta a los productores de la sierra, quienes aseguran que lo que "
     "reciben por kilo apenas alcanza para cubrir los costos de cosecha, transporte y pago de jornaleros. Los analistas "
     "explican que el mercado depende de la oferta mundial, del clima en los grandes países productores y de la "
     "especulación financiera. Cuando los precios se hunden, las familias recortan gastos, posponen el mantenimiento de "
     "las plantas y a veces dejan frutos sin cortar. Algunos buscan ingresos adicionales con la venta de café tostado y "
     "molido, o con visitas turísticas a sus fincas. Los líderes piden seguros de ingreso y apoyos que ayuden a resistir "
     "los años de cotizaciones bajas."),
    # ---------------------------------------------------------------- TURISMO
    ("turismo", "turismo-sumidero",
     "Recorridos en lancha por el Cañón del Sumidero reciben miles de visitantes",
     "El Cañón del Sumidero continúa siendo uno de los principales atractivos del estado: cada fin de semana miles de "
     "personas abordan lanchas en Chiapa de Corzo para recorrer el río Grijalva entre paredes de roca que superan los mil "
     "metros de altura. Los guías explican la formación geológica, señalan la Cueva del Silencio y la cascada conocida "
     "como Árbol de Navidad, y ayudan a identificar cocodrilos, garzas y monos araña. Los lancheros recuerdan a los "
     "pasajeros usar chaleco salvavidas y no arrojar basura al agua. Las autoridades de turismo destacan que el parque "
     "nacional necesita limitar el número de embarcaciones y reforzar la limpieza, porque la belleza del lugar también "
     "depende del cuidado diario."),
    ("turismo", "turismo-sancristobal",
     "El centro histórico de San Cristóbal de las Casas atrae viajeros con sus andadores y museos",
     "Los andadores peatonales del centro histórico de San Cristóbal de las Casas reciben a turistas nacionales y "
     "extranjeros que caminan entre casas coloniales de colores, iglesias, cafés y librerías. Los visitantes recorren el "
     "templo de Santo Domingo, el mercado de artesanías y los museos que explican la historia de los pueblos mayas de los "
     "Altos. Los comerciantes aseguran que las ventas aumentan en vacaciones, aunque lamentan que algunas calles se "
     "saturen de visitantes y vehículos. Vecinos piden regular los alquileres para evitar que los habitantes originales "
     "se vayan del barrio. Guías locales proponen rutas culturales que lleven a los viajeros a talleres de textiles, "
     "ámbar y cerámica, para repartir mejor los beneficios del turismo."),
    ("turismo", "turismo-palenque",
     "La zona arqueológica de Palenque ofrece recorridos nocturnos y visitas guiadas",
     "En medio de la selva, la zona arqueológica de Palenque ofrece visitas guiadas para conocer el Templo de las "
     "Inscripciones, el Palacio y los relieves que cuentan la historia de la antigua ciudad maya. Los arqueólogos "
     "explican que la ciudad alcanzó su esplendor en el siglo séptimo, bajo el gobierno de Pakal, y que su arquitectura "
     "destaca por las bóvedas y los techos decorados. Los guías recomiendan llegar temprano para evitar el calor y llevar "
     "agua, gorra y calzado cómodo. El sitio cuenta con un museo con piezas y ofrendas halladas en las excavaciones. Las "
     "autoridades piden respetar los senderos, no escalar los edificios y cuidar la vegetación que rodea las "
     "estructuras."),
    ("turismo", "turismo-aguaazul",
     "Las cascadas de Agua Azul y los lagos de Montebello destacan entre los destinos de naturaleza",
     "Entre los destinos de naturaleza más visitados del estado sobresalen las cascadas de Agua Azul, cuyas pozas color "
     "turquesa se forman por el carbonato de calcio disuelto en el río, y los lagos de Montebello, un conjunto de "
     "lagunas de tonos verdes y azules rodeadas de bosque. Los visitantes pueden caminar por senderos, andar en balsas o "
     "simplemente descansar en las orillas. Los pobladores indígenas que administran algunos accesos explican que en "
     "temporada de lluvias el agua se vuelve turbia y la corriente puede ser peligrosa, por lo que piden no nadar en "
     "zonas señaladas. Recomiendan llevar bloqueador biodegradable, respetar los horarios y comprar alimentos y "
     "artesanías a las familias de la comunidad."),
    ("turismo", "turismo-ecoturismo",
     "Comunidades de la Lacandona impulsan ecoturismo con cabañas y recorridos en la selva",
     "Algunas comunidades cercanas a la Selva Lacandona han desarrollado proyectos de ecoturismo que ofrecen cabañas "
     "rústicas, caminatas guiadas y observación de aves. Los habitantes aprendieron a atender visitantes, preparar "
     "alimentos locales y compartir su conocimiento sobre las plantas medicinales y el comportamiento de los animales. "
     "Los ingresos se reparten entre las familias y una parte se destina a la vigilancia contra la tala ilegal. Los "
     "viajeros duermen en hamacas, escuchan a los monos aulladores al amanecer y navegan en cayucos por las lagunas. Los "
     "organizadores subrayan que el objetivo no es llenar la selva de turistas, sino ofrecer una alternativa económica "
     "que haga más valioso conservar el bosque en pie."),
    ("turismo", "turismo-hoteles",
     "Hoteles de Chiapas reportan alta ocupación en la temporada vacacional",
     "Los hoteleros del estado informaron que la ocupación alcanzó niveles altos durante la temporada vacacional, con "
     "reservaciones llenas en Tuxtla Gutiérrez, San Cristóbal de las Casas y Palenque. Los administradores señalan que el "
     "aumento se debe a la mejor promoción de los destinos, a las ofertas de paquetes y a la llegada de familias que "
     "viajan por carretera. Restauranteros y guías también reportan ventas superiores. Sin embargo, algunos prestadores "
     "pidieron mejorar los servicios básicos, como el agua y la recolección de basura, porque la saturación pone a "
     "prueba la capacidad de los municipios. Los expertos recomiendan diversificar la oferta y promover visitas en "
     "temporada baja para que los ingresos no dependan solo de unas pocas semanas del año."),
    # ---------------------------------------------------------------- SALUD
    ("salud", "salud-dengue",
     "Alertan por aumento de casos de dengue y piden eliminar criaderos del mosquito",
     "Las autoridades sanitarias emitieron una alerta por el aumento de casos de dengue en varios municipios de la "
     "costa. La enfermedad se transmite por la picadura del mosquito Aedes aegypti, que se reproduce en agua estancada "
     "dentro y alrededor de las viviendas. Los síntomas incluyen fiebre alta, dolor de cabeza, dolor detrás de los ojos y "
     "malestar en músculos y articulaciones. Las brigadas realizan fumigación y visitas casa por casa para destruir "
     "criaderos, y piden a la población vaciar cubetas, tapar tinacos y lavar los floreros cada semana. Los médicos "
     "recomiendan acudir al hospital si hay vómito persistente, sangrado o dolor abdominal intenso, y evitar la "
     "automedicación con aspirina o antiinflamatorios."),
    ("salud", "salud-vacunacion",
     "Arranca campaña de vacunación infantil en escuelas y centros de salud",
     "Inició una campaña de vacunación dirigida a niñas y niños para completar sus esquemas contra el sarampión, la "
     "polio y otras enfermedades prevenibles. Las enfermeras instalaron módulos en escuelas, mercados y centros de salud, "
     "y recorrerán comunidades alejadas para llegar a quienes no han podido acudir. Los pediatras explican que las "
     "vacunas entrenan al sistema inmune para reconocer virus y bacterias sin enfermar al menor, y que mantener altas "
     "coberturas protege incluso a quienes no pueden vacunarse. Piden a madres y padres llevar la cartilla y no aplazar "
     "las dosis por miedo a reacciones leves como fiebre o dolor en el brazo. Las autoridades aseguran que el biológico "
     "es seguro y gratuito."),
    ("salud", "salud-hospital",
     "Amplían hospital regional para atender a más pacientes y reducir traslados",
     "La ampliación de un hospital regional permitirá atender a más pacientes sin necesidad de trasladarlos a la "
     "capital. La obra incluye nuevas camas, un área de urgencias, quirófanos y un laboratorio para estudios clínicos. "
     "Los directivos señalan que muchas familias viajaban horas para recibir atención especializada, lo que retrasaba "
     "diagnósticos y encarecía el tratamiento. Médicos y enfermeras piden que, además del equipo, se garantice personal "
     "suficiente y abasto de medicamentos, pues un edificio moderno no sirve si faltan insumos. Organizaciones sociales "
     "reclaman que la atención llegue también a las comunidades indígenas, con intérpretes en lenguas locales para "
     "explicar los diagnósticos y las indicaciones a los pacientes."),
    ("salud", "salud-nutricion",
     "Programas de alimentación combaten la desnutrición infantil en comunidades rurales",
     "Un programa de alimentación busca reducir la desnutrición infantil en comunidades rurales de la sierra y la "
     "selva. El personal de salud mide el peso y la talla de los niños, ofrece desayunos escolares y entrega "
     "suplementos de vitaminas a quienes lo necesitan. Las nutriólogas también enseñan a las familias a combinar maíz, "
     "frijol, verduras y huevo para mejorar la dieta con ingredientes accesibles, y fomentan los huertos familiares. "
     "Explican que la falta de nutrientes durante los primeros años afecta el crecimiento y el aprendizaje, por lo que la "
     "prevención temprana es clave. Los responsables reconocen que la pobreza y la distancia dificultan el acceso a "
     "alimentos variados y piden que los apoyos lleguen con regularidad."),
    ("salud", "salud-mental",
     "Crece la demanda de atención psicológica entre jóvenes y adultos",
     "Psicólogos y trabajadores sociales reportan un aumento en la demanda de atención por ansiedad, depresión y estrés "
     "entre jóvenes y adultos. Explican que la presión económica, la violencia y los cambios después de la pandemia "
     "afectaron el bienestar emocional de muchas personas. Algunas universidades abrieron módulos de orientación gratuita "
     "y líneas telefónicas para escuchar y canalizar casos urgentes. Los especialistas recomiendan hablar con familiares "
     "o amigos, mantener rutinas de sueño y ejercicio, y buscar ayuda profesional cuando la tristeza o el miedo "
     "interfieren con el trabajo o los estudios. Piden también reducir el estigma, porque todavía mucha gente cree que "
     "acudir a terapia es señal de debilidad."),
    ("salud", "salud-brigadas",
     "Brigadas de salud llegan a comunidades alejadas con consultas y medicamentos",
     "Brigadas formadas por médicos, enfermeras y dentistas recorren comunidades alejadas para ofrecer consultas, "
     "curaciones y entrega de medicamentos. En cada localidad se instala un módulo en la escuela o en el salón comunal, "
     "donde se atienden infecciones, enfermedades crónicas como diabetes e hipertensión, y control de embarazos. Los "
     "vecinos agradecen que el servicio llegue a su puerta, pues el traslado a una clínica puede costar dinero y varias "
     "horas de camino. El personal también imparte pláticas sobre higiene, lavado de manos y uso correcto de los "
     "remedios. Los coordinadores reconocen que las brigadas no sustituyen a un centro de salud permanente y piden "
     "construir clínicas y capacitar parteras y promotores comunitarios."),
    # ---------------------------------------------------------------- RIESGOS NATURALES Y CLIMA
    ("riesgos", "riesgo-sismo",
     "Sismo de magnitud 5.8 sacude la costa y deja réplicas sin daños graves",
     "Un sismo de magnitud 5.8 sacudió la costa de Chiapas durante la madrugada y se sintió con fuerza en varios "
     "municipios. El movimiento telúrico tuvo su epicentro frente al litoral y fue seguido por decenas de réplicas de "
     "menor intensidad. Protección civil informó que no se registraron víctimas, aunque se reportaron grietas en algunas "
     "viviendas antiguas y caída de objetos. Los vecinos salieron a las calles y esperaron a que cesara el temblor antes "
     "de volver a entrar. Los especialistas recuerdan que Chiapas se ubica en una zona de gran actividad sísmica por la "
     "interacción de placas tectónicas, y recomiendan revisar la estructura de las casas, tener una mochila de "
     "emergencia y conocer las rutas de evacuación."),
    ("riesgos", "riesgo-simulacro",
     "Escuelas realizan simulacro y practican protocolos de evacuación ante temblores",
     "Cientos de escuelas participaron en un simulacro para practicar qué hacer en caso de un temblor fuerte. Los "
     "alumnos aprendieron a mantener la calma, alejarse de ventanas, protegerse debajo de mesas resistentes y salir en "
     "orden hacia las zonas de seguridad. Los maestros revisaron las rutas de salida, los extintores y los "
     "señalamientos, y los brigadistas cronometraron el tiempo de desalojo. Protección civil explicó que repetir los "
     "ejercicios ayuda a reducir el pánico y a salvar vidas, porque las personas reaccionan mejor cuando ya han "
     "ensayado. También recomendó a las familias elaborar un plan de emergencia con puntos de reunión, números "
     "telefónicos y documentos importantes guardados en una bolsa de fácil acceso."),
    ("riesgos", "riesgo-tormenta",
     "Tormenta tropical amenaza la costa y autoridades preparan evacuaciones",
     "Una tormenta tropical que podría convertirse en huracán se acerca a la costa del Pacífico y mantiene en alerta a "
     "las autoridades de protección civil. Se prevén lluvias intensas, vientos fuertes y oleaje elevado, por lo que se "
     "pidió a los pescadores no salir a altamar y a las familias de zonas bajas prepararse para evacuar. Se habilitaron "
     "albergues en escuelas y salones comunitarios, con colchonetas, alimentos y atención médica. Los meteorólogos "
     "explican que el agua cálida del océano alimenta estos fenómenos y que la trayectoria puede cambiar. Recomiendan "
     "asegurar techos, almacenar agua potable, cargar teléfonos y seguir únicamente los avisos oficiales para evitar "
     "rumores y decisiones tardías."),
    ("riesgos", "riesgo-inundacion",
     "Desbordamiento de un río deja calles inundadas y familias en albergues",
     "Tras días de lluvia constante, el desbordamiento de un río provocó inundaciones en varias colonias y obligó a "
     "decenas de familias a refugiarse en albergues. El agua alcanzó más de un metro de altura en algunas calles, "
     "arrastró muebles y dañó cultivos de las orillas. Brigadistas y voluntarios ayudaron a evacuar a niños y adultos "
     "mayores en lanchas, mientras las autoridades repartían despensas y cobijas. Después de que el nivel bajó, los "
     "vecinos comenzaron a limpiar el lodo y las autoridades sanitarias pidieron hervir el agua, desinfectar los pisos y "
     "eliminar charcos para evitar enfermedades como diarrea y dengue. Los especialistas insisten en limpiar los cauces "
     "y no construir en zonas de riesgo."),
    ("riesgos", "riesgo-deslave",
     "Deslaves bloquean un tramo carretero y complican el paso de vehículos",
     "Las lluvias provocaron deslaves en cerros cercanos a una carretera de la sierra, lo que bloqueó el paso de "
     "vehículos durante varias horas. Maquinaria pesada retiró tierra, piedras y árboles caídos mientras los "
     "automovilistas esperaban en largas filas. Protección civil explicó que el agua satura el suelo, lo vuelve pesado e "
     "inestable y facilita que la ladera se desprenda, sobre todo donde se talaron árboles. Pidieron a los conductores no "
     "viajar de noche, evitar detenerse cerca de taludes y consultar el estado del camino antes de salir. Ingenieros "
     "advierten que se necesitan obras de contención y drenaje, y reforestar las laderas, para disminuir la repetición "
     "de estos accidentes en cada temporada de lluvias."),
    ("riesgos", "riesgo-calor",
     "Ola de calor eleva las temperaturas y autoridades piden hidratarse",
     "Una ola de calor elevó las temperaturas por encima de los 38 grados en varias regiones del estado, y las "
     "autoridades de salud pidieron a la población hidratarse, evitar la exposición al sol entre las once de la mañana y "
     "las cuatro de la tarde y usar ropa ligera. Los médicos advierten que los niños, los adultos mayores y los "
     "trabajadores que laboran a la intemperie son los más vulnerables al golpe de calor, cuyos signos incluyen mareo, "
     "piel enrojecida, náuseas y confusión. Algunas escuelas ajustaron horarios y habilitaron espacios con sombra. Los "
     "meteorólogos relacionan estos episodios con el cambio climático y esperan que se vuelvan más frecuentes, por lo que "
     "recomiendan planificar medidas de adaptación en las ciudades."),
]
