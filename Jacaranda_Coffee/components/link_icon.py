import reflex as rx
from Jacaranda_Coffee.styles.styles import Size
from Jacaranda_Coffee.styles.colors import Color

def link_icon(icon: str, url: str) -> rx.Component:
    return rx.link(
                rx.icon(
                    f"{icon}",
                    gap="2",
                    margin_top="3em",
                    size=40,                 
                ),  
            href=url,
            is_external=True,
            color=Color.SECONDARY.value,  
            _hover={'color': Color.CUARTIARY.value},
            align="center",  
            )
    
def link_icon_footer(icon: str, url: str) -> rx.Component:
    return rx.link(
                rx.icon(
                    f"{icon}",
                    gap="2",
                    size=30,                 
                ),
            href=url,
            is_external=True,
            color="#828282",             
            _hover={'color': Color.CUARTIARY.value},
            align="center",
            )