import reflex as rx
import Jacaranda_Coffee.styles.styles as styles
from Jacaranda_Coffee.styles.styles import Size

def title(text: str) -> rx.Component:
    return rx.heading(
        rx.hstack(
            rx.text(text),        
            ),
            align="left",
            padding=Size.SMALL.value,
            margin_top=Size.SMALL.value,
            style=styles.title_style
        )  
    
def method_title(text: str) -> rx.Component:
    return rx.heading(
        rx.hstack(
            rx.text(text),        
            ),
            align="left",
            padding_top=Size.SMALL.value,
            padding_left=Size.SMALL.value,
            padding_bottom=Size.SMALL.value,
            style=styles.method_title_style
        )   
            

 