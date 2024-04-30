import reflex as rx
from Jacaranda_Coffee.styles.colors import Color

def green_line() -> rx.Component:
    return rx.divider(
        height="4em",
        bg=Color.ACCENT.value
    )