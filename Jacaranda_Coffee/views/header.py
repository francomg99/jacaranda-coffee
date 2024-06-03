import reflex as rx
from Jacaranda_Coffee.styles.styles import Size
from Jacaranda_Coffee.styles.fonts import Font
from Jacaranda_Coffee.styles.colors import Color, TextColor
from Jacaranda_Coffee.views.carrusel import home_carousel

def header_with_image_and_text():
    return rx.hstack(
        rx.box(
            rx.text(
                "¿Quieres unirte a la verdadera", 
                align="left", 
                size="8", 
                as_="div"
            ),
            rx.text(
                "manera de vivir el ", 
                    rx.text.strong(
                        "café?", 
                        font_family=Font.DEFAULT.value
                    ), 
                align="left", 
                size="8", 
                as_="div"
            ),
            rx.button(
                    rx.icon(tag="phone"),
                    "Escribinos",
                    color=Color.TERTIARY.value,
                    bg=Color.CUARTIARY.value,
                    size="3",
                    margin_top=Size.MEDIUM.value,
                    on_click=rx.redirect(path="/"),
                    is_external=True,
                    _hover={
                        "background": Color.PRIMARY.value,
                        "color": TextColor.PRIMARY.value
                        }
                        ),
                bg="center/cover url('/bg_coffee2.jpg')",
                spacing="4",
                width="100%",
                height=["25em","37em"],
                padding_x=["1em","3em"],
                padding_y=["5em","12em"],
                top="0"
        )
    )