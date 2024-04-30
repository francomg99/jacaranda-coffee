import reflex as rx
from Jacaranda_Coffee.styles.styles import Size, Color
from Jacaranda_Coffee.components.link_icon import link_icon
from Jacaranda_Coffee.styles.fonts import Font

def navbar() -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.image(
                src="coffee_logo.png",
                alt="Imagén de una taza animada sonriendo",
                width=["8.5em","7.5em"],
            ),
            rx.heading(
                "Jacaranda Coffee", 
                font_size=[Size.BIG.value, Size.TITLE.value], 
                padding_top=["1.5em","0.75em"], 
                font_family=Font.TITLE.value, 
                weight="light",
            ),
        rx.spacer(),
            rx.tablet_and_desktop(
                rx.hstack(
                    link_icon(
                        "youtube",
                        "/"                
                    ),
                    link_icon(
                        "twitter",
                        "/"
                    ),
                    link_icon(
                        "twitch",
                        "/"
                    )
                )
            ),
            width="100%"
        ),
        bg=Color.ACCENT.value,
        position="sticky",
        padding_x=Size.BIG.value,
        padding_y=Size.SMALL.value,
        z_index="999",
        top="0",
        width="100%",
        align="center"
    )
