import reflex as rx
from Jacaranda_Coffee.components.icons import icon
from Jacaranda_Coffee.styles.colors import Color
from Jacaranda_Coffee.styles.styles import Size


def info() -> rx.Component:
    return rx.chakra.responsive_grid(
                icon(
                    "coffee",
                    "Conoce todas las propiedades",
                    "que te brinda"
                ),
                icon(
                    "clock",
                    "No pierdas tu tiempo y",
                    "elije un buen café"
                ),
                icon(
                    "heart",
                    "Tu salud es lo primero.",
                    "Toma un café de calidad."
                ),
                columns=[1, 3],
                padding=Size.VERY_BIG.value,
                bg=Color.PRIMARY.value,
                spacing="2",
                width="100%",
                height="auto",
            )
       