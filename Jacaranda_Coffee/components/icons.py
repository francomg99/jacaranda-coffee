import reflex as rx
from Jacaranda_Coffee.styles.styles import Size


def icon(icon: str, text: str, text_2: str):
    return rx.flex(
        rx.icon(icon, size=80),
        rx.text(text, align="center",font_size=Size.DEFAULT.value),
        rx.text(text_2, align="center",font_size=Size.DEFAULT.value),
        direction="column",
        align_items="center",
        gap="1",
        padding=Size.MEDIUM.value
    )
