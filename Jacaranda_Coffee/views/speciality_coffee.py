import reflex as rx
from Jacaranda_Coffee.components.title import title
from Jacaranda_Coffee.styles.styles import Size
from Jacaranda_Coffee.styles.colors import Color, TextColor

def speciality_coffee() -> rx.Component:
    return rx.vstack(
            title("Café de Especialidad"),
            rx.box(
                rx.text(
                    """Es muy común relacionar el café de especialidad con un café especial, 
                    pero eso no es así. Cuando se habla de café de especialidad, 
                    se hacer referencia al café de una calidad extraordinaria por su cuidadosa 
                    selección de granos de café. Para recibir esta denominación, el café ha tenido que 
                    obtener 80 o más puntos en una categoría que llega hasta los 100 puntos.""",
                margin_bottom=Size.DEFAULT.value,
                style={
                    "text-indent": Size.MEDIUM.value,
                    "font_size":Size.DEFAULT.value
                }
                ),
                rx.tablet_and_desktop(
                rx.hstack(
                    rx.image(
                        src="guia_cafe.jpg",
                        alt="Tabla de sabores de café de especialidad con una taza",
                        width="35%",
                        padding_top=Size.SMALL.value
                        
                    ),
                    rx.spacer(),
                    rx.vstack(
                        rx.text(
                            """Las dos variedades principales son el café arábica y el café robusta. 
                            Casi la totalidad del café de especialidad se compone solo de café arábica. 
                            En contadas ocasiones se utiliza café de la variedad robusta, 
                            pero solo aquel cultivado en zonas cálidas y de altura, como el arábica.""",
                            margin_left=Size.DEFAULT.value,
                            style={
                                "text-indent": Size.MEDIUM.value,
                                "font_size":Size.DEFAULT.value
                            }
                        ),
                        rx.text(
                            """
                            La idoneidad del café arábica para cafés de especialidad se basa 
                            en su perfecto equilibrio entre sabor y cuerpo. Los cafetos de café de especialidad 
                            se plantan, además, en condiciones de sol y sombra.""",
                            margin_left=Size.DEFAULT.value,
                            style={
                                "text-indent": Size.MEDIUM.value,
                                "font_size":Size.DEFAULT.value
                            }
                        ),
                        rx.button(
                        rx.icon(tag="coffee"),
                        "SABER MÁS",
                        color=Color.CUARTIARY.value,
                        bg=Color.PRIMARY.value,
                        size="3",
                        margin_left=Size.BIG.value,
                        on_click=rx.redirect(path="https://www.youtube.com"),
                        is_external=True,
                        _hover={
                            "background": Color.SECONDARY.value,
                            "color": TextColor.PRIMARY.value
                        }
                        ),
                    )
                )    
                ),  
                rx.mobile_only(
                        rx.button(
                        rx.icon(tag="coffee"),
                        "SABER MÁS",
                        color=Color.CUARTIARY.value,
                        bg=Color.PRIMARY.value,
                        size="3",
                        mpadding=Size.BIG.value,
                        on_click=rx.redirect(path="/"),
                        is_external=True,
                        _hover={
                            "background": Color.SECONDARY.value,
                            "color": TextColor.PRIMARY.value
                        }
                        ),
                        ),             
                width="100%",
                padding_left=Size.DEFAULT.value,
                padding_right=Size.DEFAULT.value,
                padding_bottom=Size.VERY_BIG.value,               
                align="left",
                
            )
        )        
    