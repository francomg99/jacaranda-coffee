import reflex as rx
from Jacaranda_Coffee.components.title import title, method_title
from Jacaranda_Coffee.styles.styles import Size, TextColor, Color
from Jacaranda_Coffee.components.mas_info import mas_info

def metods() -> rx.Component:
    return rx.vstack(
       title("Métodos de preparación"),
            rx.vstack(
                method_title("Máquina de espresso"),
                rx.text(
                    """¿En qué consiste un espresso? 
                    Espresso es el nombre que obtiene el método 
                    para hacer café, es decir, cuando una pequeña cantidad de agua 
                    es forzada a través de café finamente molido, bajo una intensa presión 
                    en muy poco tiempo, obteniendo como resultado, una bebida corta.""",
                    width="99%",
                    padding_left=Size.SMALL.value,
                    align="left",
                    style={
                        "text-indent": Size.DEFAULT.value,                        
                        "font_size":Size.DEFAULT.value
                        },
                ),
                mas_info(
                    "Maquina de Espresso",
                    """Las máquinas de espresso son dispositivos que extraen café espresso al pasar agua caliente a alta presión 
                    a través de café molido finamente. Además de espresso, pueden preparar bebidas como cappuccinos y lattes, satisfaciendo las 
                    preferencias de los amantes del café.""",
                    """El espresso es una parte esencial de la cultura del café y estas máquinas permiten disfrutar de esta bebida en casa 
                    o en establecimientos especializados. Han evolucionado para ofrecer mayor calidad y consistencia en la preparación del café, 
                    siendo valoradas por su capacidad para producir café de alta calidad con un sabor y aroma excepcionales.""",
                    """Tanto en hogares como en cafeterías, las máquinas de espresso son apreciadas por su papel indispensable en la creación 
                    de la experiencia del café espresso, reflejando su importancia en la cultura del café contemporánea.""",
                    "espresso_machine.png",
                    "Imagen de una Maquina de Espresso."                    
                ),
                    align_items="left",
                    justify_content="left",
                    spacing="4",
            ),
                method_title("Moka Italiana"),
                rx.text(
                    """Una cafetera italiana, también conocida como cafetera moka, 
                    es un utensilio de cocina utilizado para preparar café espresso. 
                    Consiste en tres partes principales: una cámara inferior para el agua, 
                    una cámara intermedia para el café molido y un filtro, y una cámara superior 
                    para recoger el café hecho.""",
                    width="99%",
                    padding_left=Size.SMALL.value,
                    align="left",
                    style={
                        "text-indent": Size.DEFAULT.value,                        
                        "font_size":Size.DEFAULT.value
                        },
                ),
                mas_info(
                    "Moka Italiana",
                    """La Moka italiana es una cafetera clásica de diseño simple, compuesta por tres partes: 
                    una base para el agua, un filtro para el café molido y una cámara superior para el café preparado.  
                    Utilizando el principio de la presión del vapor, esta cafetera produce un café fuerte y aromático que es 
                    apreciado por su sabor distintivo.""",
                    """Su popularidad se debe a su facilidad de uso y al rico café que produce. 
                    La Moka italiana es un elemento común en muchos hogares, especialmente en Italia, 
                    donde forma parte de la rutina diaria. Aunque han surgido nuevas tecnologías en la preparación del café, 
                    la Moka sigue siendo apreciada por su simplicidad y su capacidad para crear una experiencia de café única.""",
                    """A lo largo de los años, la Moka italiana ha experimentado algunas modificaciones en su diseño, 
                    pero su esencia sigue siendo la misma. Permanece como un símbolo de la artesanía y la tradición italiana 
                    en el arte de hacer café.""",
                    "italian_moka.png",
                    "Imagen de una Moka Italiana."
                ),
                method_title("Prensa Francesa"),
                rx.text(
                    """La prensa francesa es un método de extracción por inmersión total. 
                    Es decir, el café y el agua están en contacto constante por un tiempo determinado. 
                    Luego, se filtra a través de una malla metálica. Con la prensa francesa podemos preparar 
                    cualquier variedad de café y destacar los aspectos más interesantes de cada uno.""",
                    width="99%",
                    padding_left=Size.SMALL.value,
                    align="left",
                    style={
                        "text-indent": Size.DEFAULT.value,                        
                        "font_size":Size.DEFAULT.value
                        },
                ),
                mas_info(
                    "Prensa Francesa",
                    """La prensa francesa, también llamada cafetera de émbolo, es un dispositivo simple para hacer café. 
                    Consta de un recipiente con un émbolo y un filtro de malla. Este método extrae los aceites y sabores del café molido, 
                    produciendo una bebida rica y con cuerpo.""",
                    """Para preparar café con una prensa francesa, se agrega café molido al recipiente, se vierte agua caliente y se deja reposar.
                    Luego, se presiona lentamente el émbolo hacia abajo para filtrar el café. El resultado es una taza de café intenso y sedoso.""",
                    """La prensa francesa es apreciada por su simplicidad y la calidad del café que produce. Es una opción popular entre 
                    los amantes del café que buscan una experiencia auténtica y satisfactoria. Siendo muy popular en las cafeterías modernas aún.""",
                    "french_press.png",
                    "Imagen de una Prensa Francesa."
                ),
                    align_items="left",
                    justify_content="left",
                    spacing="4",
            )

    
