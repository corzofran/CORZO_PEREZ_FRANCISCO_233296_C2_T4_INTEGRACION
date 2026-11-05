"""Corpus sintético (parte B): tecnología, infraestructura, ambiente, economía y cultura/gastronomía.

Los textos fueron REDACTADOS para este proyecto (no provienen de ninguna fuente externa). Los lugares son reales
(Chiapas, México), pero los sucesos descritos son ilustrativos. Cada entrada: (tema, subtema, titulo, texto).
"""

DOCS_B = [
    # ---------------------------------------------------------------- TECNOLOGÍA Y EDUCACIÓN
    ("tecnologia", "tec-ia",
     "Laboratorio universitario de inteligencia artificial entrena modelos para analizar textos en español",
     "Un laboratorio de una universidad tecnológica trabaja con inteligencia artificial para analizar textos en español, "
     "como noticias, encuestas y mensajes de atención ciudadana. Los estudiantes entrenan modelos de aprendizaje "
     "automático que clasifican temas, detectan opiniones y resumen documentos. Para ello usan computadoras con tarjetas "
     "gráficas, bibliotecas de código abierto y conjuntos de datos revisados manualmente. Los asesores explican que la "
     "calidad del resultado depende de la calidad de los datos, y que es necesario medir errores y sesgos antes de usar "
     "un modelo en la vida real. El laboratorio planea colaborar con dependencias locales para organizar archivos y "
     "facilitar búsquedas, y abrir cursos para que más jóvenes aprendan los fundamentos de la ciencia de datos."),
    ("tecnologia", "tec-robotica",
     "Equipos escolares compiten en un torneo de robótica con brazos y vehículos autónomos",
     "Estudiantes de secundaria y preparatoria participaron en un torneo de robótica donde presentaron brazos mecánicos, "
     "vehículos autónomos y robots que siguen líneas. Cada equipo diseñó, armó y programó su prototipo con sensores, "
     "motores y placas electrónicas, y enfrentó pruebas de precisión y velocidad. Los jueces destacaron la creatividad "
     "de los jóvenes y la forma en que resolvieron fallas durante el evento. Los maestros señalan que la robótica enseña "
     "matemáticas, física y trabajo en equipo de manera práctica. Los participantes agradecieron el apoyo de sus escuelas "
     "y pidieron más talleres y materiales. Los organizadores esperan que el torneo motive vocaciones en ingeniería y "
     "que algunos equipos representen al estado en competencias nacionales."),
    ("tecnologia", "tec-bootcamp",
     "Bootcamp gratuito de programación y ciencia de datos recibe cientos de solicitudes",
     "Un programa gratuito de programación y ciencia de datos recibió cientos de solicitudes de jóvenes interesados en "
     "aprender a escribir código y analizar información. El curso intensivo incluye clases de Python, bases de datos, "
     "estadística y proyectos prácticos, y se imparte en línea con tutorías presenciales. Los instructores explican que "
     "muchas empresas buscan personas que sepan limpiar datos, construir tableros y automatizar tareas, y que no es "
     "indispensable tener un título para empezar. Las y los participantes trabajarán en un proyecto final con datos "
     "públicos del estado, como precipitación, precios agrícolas y registros de salud. Los organizadores esperan que los "
     "egresados consigan prácticas, empleos remotos o inicien sus propios negocios digitales."),
    ("tecnologia", "tec-internet",
     "Instalan antenas para llevar internet a comunidades rurales sin cobertura",
     "Una iniciativa de conectividad instaló antenas y puntos de acceso para llevar internet a comunidades rurales que "
     "carecían de cobertura. Los técnicos capacitaron a vecinos para dar mantenimiento a los equipos y administrar el "
     "servicio, que funciona con paneles solares y enlaces inalámbricos. Los maestros ya usan la conexión para descargar "
     "materiales y comunicarse con otras escuelas, y las familias hacen videollamadas con parientes que trabajan lejos. "
     "Los líderes comunitarios señalan que el acceso permite consultar precios de cultivos, realizar trámites y atender "
     "a estudiantes en línea. También advierten sobre la importancia de enseñar seguridad digital y evitar fraudes. El "
     "principal reto será sostener el costo del enlace satelital a largo plazo."),
    ("tecnologia", "tec-app",
     "Jóvenes emprendedores desarrollan una aplicación móvil para pequeños agricultores",
     "Un equipo de jóvenes emprendedores desarrolló una aplicación móvil que ayuda a pequeños agricultores a consultar el "
     "clima, registrar sus gastos y conocer los precios de venta de sus productos. La herramienta funciona con poca "
     "conexión y ofrece mensajes de voz para las personas que leen con dificultad. Los creadores probaron el prototipo "
     "con productores de café y maíz, quienes sugirieron incluir alertas de plagas y un directorio de compradores. "
     "Cuentan que aprendieron a programar en cursos en línea y que consiguieron un pequeño capital en un concurso de "
     "innovación. Ahora buscan alianzas con cooperativas y con instituciones educativas para mejorar la aplicación, "
     "ampliar su alcance y demostrar que la tecnología puede resolver problemas del campo."),
    ("tecnologia", "tec-becas",
     "Entregan becas para estudiantes de ingeniería y carreras tecnológicas",
     "Cientos de estudiantes de ingeniería y carreras tecnológicas recibieron becas que cubren colegiaturas, transporte y "
     "compra de equipo de cómputo. Las autoridades educativas explican que el apoyo busca reducir la deserción, sobre "
     "todo entre jóvenes de comunidades rurales que deben recorrer largas distancias o trabajar para sostenerse. Para "
     "conservar la beca, los alumnos deben mantener un promedio mínimo y participar en actividades de servicio "
     "comunitario. Algunos beneficiarios cuentan que podrán dedicar más tiempo a sus proyectos de software y "
     "electrónica, y otros planean realizar estancias en laboratorios. Los empresarios locales ofrecieron prácticas "
     "profesionales y pidieron que las universidades actualicen sus planes de estudio con herramientas actuales de "
     "programación y análisis de datos."),
    # ---------------------------------------------------------------- INFRAESTRUCTURA Y TRANSPORTE
    ("infraestructura", "infra-carretera",
     "Modernizan una carretera de montaña y reducen el tiempo de traslado entre municipios",
     "La modernización de una carretera de montaña ya permite que los traslados entre dos municipios se reduzcan casi a "
     "la mitad. La obra incluyó ampliación de carriles, nueva carpeta asfáltica, señalamientos reflectantes y cunetas "
     "para desalojar el agua. Los transportistas aseguran que ahora pueden llevar el café, el maíz y el ganado con menos "
     "riesgo de accidentes y menor desgaste de sus camiones. Los habitantes cuentan que antes los baches y el lodo "
     "dejaban incomunicados a varios poblados durante la temporada de lluvias. Aun así, ingenieros recuerdan que una "
     "carretera necesita mantenimiento constante y piden vigilar el estado de los taludes. Los vecinos solicitan que "
     "también se mejoren los caminos rurales que conectan con la vía principal."),
    ("infraestructura", "infra-puente",
     "Un nuevo puente sobre el río Grijalva conectará a comunidades aisladas",
     "La construcción de un puente sobre el río Grijalva conectará a comunidades que durante años dependieron de lanchas "
     "y cuerdas para cruzar. La estructura, de concreto y acero, tendrá carril para vehículos y pasillo para peatones, y "
     "está diseñada para resistir crecidas y sismos. Los habitantes esperan que el puente facilite que los niños lleguen "
     "a la escuela, que los enfermos sean trasladados con rapidez y que los productores vendan sus cosechas en mejores "
     "condiciones. Los ingenieros explican que se realizaron estudios del suelo y del caudal para elegir la ubicación y "
     "que se instalarán sensores para vigilar su estado. Los pobladores piden que durante la obra se contrate mano de "
     "obra local y se respeten los sitios de pesca."),
    ("infraestructura", "infra-aeropuerto",
     "El aeropuerto estatal estrena rutas y busca atraer inversión y turismo",
     "El aeropuerto estatal estrenó nuevas rutas aéreas que conectan a la entidad con otras ciudades del país y buscan "
     "atraer turismo e inversión. Los directivos indican que se ampliaron la terminal, la zona de abordaje y el "
     "estacionamiento, y que se reforzaron los servicios de seguridad. Los empresarios turísticos consideran que los "
     "vuelos directos reducen el costo y el tiempo de viaje, lo que puede aumentar la llegada de visitantes extranjeros. "
     "Los productores de café y frutas esperan usar la carga aérea para enviar productos frescos a mercados lejanos. Sin "
     "embargo, urgen a mejorar los accesos terrestres y el transporte público hacia la terminal, para que los pasajeros "
     "lleguen con facilidad y los beneficios se extiendan a la población."),
    ("infraestructura", "infra-transporte",
     "Estrenan rutas de transporte público para reducir el tráfico en la capital",
     "La capital chiapaneca estrenó rutas de transporte público con unidades más modernas, paradas señalizadas y horarios "
     "más regulares. El objetivo es reducir el tráfico, disminuir la contaminación y ofrecer a los trabajadores y "
     "estudiantes una opción segura y económica. Los choferes recibieron capacitación en manejo y trato al usuario, y las "
     "unidades cuentan con espacios para personas con discapacidad. Los usuarios elogian el servicio, aunque piden que "
     "se amplíen las rutas hacia las colonias periféricas y que el boleto siga siendo accesible. Los urbanistas "
     "recuerdan que no basta con comprar camiones: se necesita planear las rutas, mantener las calles en buen estado y "
     "ordenar a los vehículos que compiten por pasaje."),
    ("infraestructura", "infra-ciclovia",
     "Proponen ciclovías y calles peatonales para mejorar la movilidad urbana",
     "Colectivos ciudadanos y especialistas en movilidad proponen construir ciclovías y calles peatonales para que las "
     "personas puedan moverse de manera segura sin depender del automóvil. Argumentan que la bicicleta es una "
     "alternativa económica, saludable y sin emisiones para trayectos cortos, siempre que existan carriles protegidos y "
     "estacionamientos seguros. Los comerciantes temen perder clientes, pero estudios en otras ciudades muestran que las "
     "zonas peatonales suelen aumentar las ventas. Los urbanistas sugieren iniciar con pruebas piloto los domingos, "
     "medir resultados y escuchar a los vecinos. También piden mejorar banquetas, semáforos y cruces para peatones, y "
     "capacitar a los conductores en el respeto a los ciclistas, porque una ciclovía sola no resuelve la inseguridad "
     "vial."),
    ("infraestructura", "infra-solar",
     "Paneles solares abastecen de energía eléctrica a poblados sin conexión a la red",
     "Un proyecto instaló paneles solares en poblados que no tenían conexión a la red eléctrica, de modo que ahora las "
     "familias cuentan con luz para estudiar, cocinar y conservar alimentos. Cada sistema incluye paneles, una batería y "
     "focos eficientes, y el mantenimiento está a cargo de técnicos locales capacitados. Los habitantes cuentan que antes "
     "dependían de velas y lámparas de petróleo, que resultaban costosas y peligrosas. Ahora los niños hacen tarea por "
     "las noches y algunos negocios pequeños pueden usar refrigeradores. Los especialistas recuerdan que la energía "
     "solar reduce las emisiones y es adecuada para zonas remotas, aunque se requieren baterías de buena calidad y "
     "planes para reciclarlas al terminar su vida útil."),
    # ---------------------------------------------------------------- MEDIO AMBIENTE Y BIODIVERSIDAD
    ("ambiente", "amb-lacandona",
     "Conservan la Selva Lacandona con vigilancia comunitaria y monitoreo satelital",
     "La Selva Lacandona, una de las regiones con mayor biodiversidad de México, se vigila con ayuda de comunidades y con "
     "imágenes satelitales que permiten detectar cambios en la cobertura forestal. Los guardabosques recorren senderos "
     "para identificar tala ilegal, incendios y cacería furtiva, y reportan sus hallazgos a las autoridades "
     "ambientales. Biólogos explican que la selva alberga miles de especies de plantas, aves, mamíferos e insectos, y "
     "que regula el clima y la disponibilidad de agua en toda la región. Los habitantes piden alternativas económicas, "
     "como el ecoturismo y la producción de miel, para no depender de la agricultura que se expande sobre el bosque. La "
     "conservación, subrayan, solo funciona si beneficia a quienes viven en el territorio."),
    ("ambiente", "amb-jaguar",
     "Registran jaguares y tapires con cámaras trampa en áreas protegidas",
     "Cámaras trampa instaladas en áreas protegidas captaron imágenes de jaguares, tapires, pumas y otras especies en "
     "peligro de extinción. Los investigadores explican que estos registros permiten estimar cuántos individuos habitan "
     "una zona y cómo se desplazan entre fragmentos de selva. El jaguar, el felino más grande del continente, necesita "
     "territorios amplios y sufre por la pérdida de su hábitat y la cacería. Los biólogos recomiendan crear corredores "
     "biológicos que conecten las áreas conservadas y trabajar con ganaderos para evitar conflictos con los animales "
     "silvestres. También destacan la importancia de proteger a las aves, como el quetzal, y de educar a los niños para "
     "que valoren la fauna local y no compren animales traficados."),
    ("ambiente", "amb-reforestacion",
     "Viveros comunitarios reforestan laderas con árboles nativos",
     "Viveros comunitarios producen miles de plántulas de árboles nativos que se siembran en laderas erosionadas y zonas "
     "deforestadas. Los habitantes recolectan semillas, preparan sustrato, riegan las plantas y las trasladan al terreno "
     "al comenzar las lluvias. Los técnicos forestales explican que usar especies de la región mejora la supervivencia "
     "de los árboles y ayuda a recuperar la fauna, los suelos y la capacidad de retener agua. Las familias reciben un "
     "pago por cuidar las plantaciones durante varios años y vigilar que no se quemen. Los participantes cuentan que ya "
     "observan menos deslaves y que han regresado aves e insectos polinizadores. Los organizadores piden constancia y "
     "financiamiento, pues reforestar no consiste solo en plantar, sino en cuidar."),
    ("ambiente", "amb-residuos",
     "Programa de reciclaje y manejo de residuos reduce la basura en las ciudades",
     "Un programa de manejo de residuos busca reducir la basura que llega a los tiraderos mediante la separación en "
     "origen, el reciclaje y la composta. Los camiones recolectores pasan en días distintos para orgánicos e "
     "inorgánicos, y los centros de acopio reciben plástico, vidrio, papel y metales. Las autoridades explican que gran "
     "parte de los desechos domésticos son restos de comida que pueden transformarse en abono, y que reciclar disminuye "
     "la contaminación y genera ingresos para los recolectores. Los vecinos señalan que al principio fue difícil "
     "acostumbrarse, pero que con talleres y vigilancia el sistema mejora. Ambientalistas piden prohibir las bolsas y "
     "envases desechables, y exigir a las empresas que se responsabilicen de sus empaques."),
    ("ambiente", "amb-manglar",
     "Protegen manglares de la costa para frenar la erosión y cuidar la pesca",
     "Comunidades de la costa trabajan para proteger los manglares, bosques de raíces en el agua que sirven de refugio a "
     "peces, camarones, cangrejos y aves. Los pescadores explican que cuando se talan los mangles disminuyen las "
     "capturas, porque desaparecen las zonas de crianza. Los biólogos agregan que estas plantas frenan la fuerza de las "
     "marejadas y de las tormentas, y almacenan grandes cantidades de carbono. Las cooperativas limpian canales, siembran "
     "propágulos y vigilan que no se rellenen los humedales para construir. También promueven recorridos en lancha para "
     "observar garzas y cocodrilos. Los líderes piden respaldo legal y apoyos económicos para sostener la vigilancia, y "
     "señalan que la salud de la laguna es la base de su alimentación e ingresos."),
    ("ambiente", "amb-rio",
     "Detectan contaminación en un río y piden sanear las descargas de aguas residuales",
     "Estudios de calidad del agua detectaron contaminación en un río que cruza varias comunidades, atribuida a descargas "
     "de aguas residuales sin tratamiento y a residuos sólidos arrojados a su cauce. Los resultados muestran presencia de "
     "bacterias y bajo nivel de oxígeno, lo que afecta a peces y otros organismos. Habitantes que usan el río para lavar "
     "ropa y bañarse reportan irritaciones en la piel y enfermedades estomacales. Especialistas recomiendan construir "
     "plantas de tratamiento, conectar las viviendas al drenaje y vigilar a las industrias. Los vecinos organizaron "
     "jornadas de limpieza y piden que las autoridades sancionen a quienes contaminan. Recuperar el río, concluyen, es "
     "una tarea compartida que exige inversión, educación y vigilancia constante."),
    # ---------------------------------------------------------------- ECONOMÍA Y COMERCIO
    ("economia", "eco-mango",
     "Productores de mango y plátano del Soconusco buscan nuevos mercados de exportación",
     "Los productores de mango y plátano de la región del Soconusco buscan abrir nuevos mercados de exportación para "
     "fruta fresca. Explican que cumplir con los estándares de inocuidad, empaque y transporte en frío es indispensable "
     "para vender en el extranjero, y que muchos pequeños agricultores necesitan asesoría y financiamiento para "
     "lograrlo. Las empacadoras seleccionan la fruta por tamaño, color y madurez, y la lavan y tratan antes de cargarla "
     "en contenedores refrigerados. Los comercializadores señalan que los precios varían según la temporada y la "
     "competencia de otros países, por lo que conviene diversificar los destinos. Los agricultores piden carreteras en "
     "buen estado y trámites aduanales ágiles para que la fruta llegue fresca y a tiempo."),
    ("economia", "eco-mercado",
     "Los mercados tradicionales mantienen su importancia pese a las tiendas de autoservicio",
     "Los mercados tradicionales siguen siendo un espacio clave para el comercio de alimentos, hierbas, artesanías y "
     "productos cotidianos, aunque compiten con las tiendas de autoservicio. Los locatarios aseguran que ofrecen "
     "productos frescos, trato directo y precios negociables, y que sus ventas se mantienen gracias a clientes fieles. "
     "Sin embargo, reconocen problemas como instalaciones deterioradas, falta de estacionamiento y competencia del "
     "comercio ambulante. Las autoridades anunciaron programas de remodelación, mejor recolección de basura y "
     "capacitación en pagos digitales. Los consumidores valoran la variedad de frutas y verduras locales, y los "
     "comerciantes confían en que un mercado limpio, seguro y bien organizado seguirá atrayendo a familias y turistas "
     "que buscan sabores y productos auténticos."),
    ("economia", "eco-remesas",
     "Las remesas sostienen la economía de miles de familias chiapanecas",
     "Los envíos de dinero de familiares que trabajan en otras ciudades o en el extranjero sostienen la economía de "
     "miles de hogares. Las remesas se destinan principalmente a alimentación, vivienda, salud y educación, y en algunos "
     "casos a pequeños negocios. Los especialistas explican que estos recursos aumentan el consumo local, pero también "
     "hacen que muchas comunidades dependan de ingresos externos. Recomiendan que las familias abran cuentas de ahorro, "
     "comparen comisiones y destinen una parte a inversiones productivas. Las cooperativas de ahorro ofrecen cursos de "
     "educación financiera y microcréditos para quienes desean iniciar un negocio. Los migrantes, por su parte, piden "
     "más seguridad en las rutas y mejores condiciones laborales, porque su esfuerzo mantiene vivas muchas "
     "comunidades."),
    ("economia", "eco-artesanas",
     "Mujeres artesanas forman una cooperativa y acceden a microcréditos",
     "Un grupo de mujeres artesanas formó una cooperativa para comprar materiales en conjunto, fijar precios justos y "
     "vender sus bordados y textiles en ferias y tiendas en línea. Con apoyo de una organización civil recibieron "
     "microcréditos de bajo interés y capacitación en administración, fotografía de producto y atención al cliente. Las "
     "socias explican que antes vendían a intermediarios que pagaban muy poco por semanas de trabajo, y que ahora "
     "conocen sus costos y pueden decidir cuánto cobrar. Los ingresos les permiten pagar la escuela de sus hijos y "
     "mejorar sus viviendas. Aun así, enfrentan desafíos como las copias industriales de sus diseños, y piden que se "
     "protejan legalmente los patrones tradicionales de sus comunidades."),
    ("economia", "eco-frontera",
     "El comercio fronterizo con Guatemala se reactiva con nuevos controles aduanales",
     "El comercio en la frontera sur con Guatemala se reactivó con la modernización de los controles aduanales y nuevas "
     "ventanillas para trámites. Los transportistas indican que los tiempos de espera disminuyeron, aunque todavía hay "
     "filas durante la temporada alta. Los productos que más circulan son frutas, granos, materiales de construcción y "
     "artículos de consumo, y muchos comerciantes pequeños cruzan a diario con mercancía. Las autoridades aseguran que "
     "la revisión se reforzó para evitar el contrabando y proteger a los trabajadores migrantes. Empresarios de ambos "
     "lados piden reglas claras, puentes en buen estado y menos burocracia, y señalan que la cooperación en seguridad y "
     "en infraestructura es indispensable para que el intercambio beneficie a las comunidades fronterizas."),
    ("economia", "eco-empleo",
     "Capacitación laboral busca emplear a jóvenes en empresas formales",
     "Un programa de capacitación laboral prepara a jóvenes para ocupar puestos en empresas formales de comercio, "
     "turismo, construcción y servicios. Los cursos incluyen atención al cliente, manejo de herramientas, nociones de "
     "contabilidad y habilidades como puntualidad y trabajo en equipo. Las empresas participantes ofrecen prácticas "
     "pagadas y, a quienes concluyen, la posibilidad de ser contratados. Los jóvenes cuentan que la falta de "
     "experiencia y de contactos les impedía conseguir empleo, y que el programa les da confianza y un certificado. Los "
     "especialistas advierten que, además de capacitar, se necesitan salarios dignos, seguridad social y oportunidades "
     "en las comunidades de origen, para que los jóvenes no se vean obligados a migrar."),
    # ---------------------------------------------------------------- CULTURA Y GASTRONOMÍA
    ("cultura", "cult-pozol",
     "El pozol, la bebida tradicional que refresca las jornadas de calor",
     "El pozol es una bebida tradicional elaborada con masa de maíz fermentada que se disuelve en agua fría y se toma "
     "durante las jornadas de calor. En muchas comunidades se prepara con cacao, y se sirve en un jícaro o en un vaso "
     "grande, con sal, chile o azúcar según el gusto. Las cocineras explican que el maíz se cuece con cal, se muele y se "
     "forma en bolas que se envuelven en hojas; con el paso de los días fermentan y adquieren un sabor ácido. Los "
     "campesinos lo llevan a sus parcelas porque sacia y da energía. Los nutriólogos señalan que aporta carbohidratos y "
     "minerales, y recomiendan prepararlo con agua limpia y conservar bien la masa para evitar enfermedades "
     "estomacales."),
    ("cultura", "cult-tamales",
     "Los tamales de chipilín, un sabor imprescindible en las mesas chiapanecas",
     "Los tamales de chipilín, una hierba aromática que se mezcla con la masa de maíz y queso, forman parte de la cocina "
     "tradicional del estado. Las cocineras explican que la masa se bate con manteca hasta que flota en agua, se "
     "extiende sobre hojas de maíz o de plátano y se rellena de queso fresco, pollo o puerco, antes de cocerse al "
     "vapor. Los tamales se preparan en bodas, fiestas patronales y reuniones familiares, y suelen acompañarse con café "
     "o chocolate caliente. Los restauranteros destacan que la cocina local utiliza ingredientes de la milpa como el "
     "frijol, la calabaza y los chiles, y que preservar las recetas es una forma de proteger la identidad cultural de la "
     "región."),
    ("cultura", "cult-marimba",
     "La marimba sigue sonando en plazas y festivales como símbolo de identidad",
     "La marimba, un instrumento de teclas de madera que se toca con baquetas, sigue sonando en plazas, bodas y "
     "festivales como símbolo de la identidad chiapaneca. Los marimbistas explican que cada tecla se afina para producir "
     "una nota, y que bajo ellas se colocan resonadores que amplifican el sonido. Es común que varios músicos toquen un "
     "mismo instrumento, mientras otros acompañan con contrabajo, guitarra y percusiones. Escuelas de música ofrecen "
     "clases para niños y jóvenes, y colectivos organizan conciertos gratuitos los fines de semana. Los artesanos que "
     "construyen marimbas lamentan que escaseen las maderas finas y piden que se cuiden los bosques. Para los "
     "aficionados, escuchar una marimba es volver a las fiestas de la infancia."),
    ("cultura", "cult-textiles",
     "Tejedoras mantienen vivo el telar de cintura y los bordados tradicionales",
     "Tejedoras de comunidades de los Altos mantienen vivo el telar de cintura y los bordados que identifican a cada "
     "pueblo. Los diseños incluyen flores, animales y figuras geométricas que tienen significado cultural y se "
     "transmiten de madres a hijas. Una prenda puede requerir semanas de trabajo, desde teñir el hilo con tintes "
     "naturales hasta tejer cada franja con paciencia. Las artesanas lamentan que los clientes regateen y que otras "
     "fábricas copien sus patrones con telas industriales. Por ello promueven etiquetas de origen, ferias donde se "
     "explica el trabajo y ventas directas que eviten intermediarios. Los jóvenes de la comunidad aprenden la técnica, y "
     "algunos diseñan ropa contemporánea sin perder los símbolos tradicionales."),
    ("cultura", "cult-fiesta",
     "La Fiesta Grande de Chiapa de Corzo llena de colores y música las calles",
     "Cada enero, Chiapa de Corzo celebra una fiesta tradicional en la que participan danzantes, músicos, cocineras y "
     "cofradías. Los Parachicos, que usan máscaras de madera, sombreros de ixtle y sarapes de colores, bailan por las "
     "calles al ritmo de pitos y tambores mientras sacuden sus chinchines. Hay procesiones, comida compartida y "
     "representaciones que recuerdan la historia local. Los organizadores explican que la fiesta se transmite de "
     "generación en generación y que las familias preparan sus trajes con meses de anticipación. Los visitantes pueden "
     "probar platillos como el cochito horneado y disfrutar de la marimba. Las autoridades piden respetar a los "
     "danzantes, cuidar los espacios públicos y apoyar a los artesanos que elaboran máscaras e instrumentos."),
    ("cultura", "cult-ambar",
     "El ámbar de Chiapas, una joya natural que se talla en talleres artesanales",
     "El ámbar de Chiapas es una resina fósil de millones de años que se extrae en minas de la sierra norte y se talla "
     "en talleres artesanales para convertirla en collares, anillos y figuras. Los artesanos explican que cada pieza es "
     "distinta, con tonos que van del amarillo al rojo y, en ocasiones, con insectos o plantas atrapados en su interior. "
     "Para trabajarlo lo lijan con paciencia y lo pulen hasta que brilla. Los vendedores recomiendan comprobar su "
     "autenticidad, porque existen imitaciones de plástico, y comprar en tiendas que muestren su origen. En San "
     "Cristóbal de las Casas hay un museo que explica su formación y su historia, y los mineros piden condiciones seguras "
     "para su trabajo."),
]
