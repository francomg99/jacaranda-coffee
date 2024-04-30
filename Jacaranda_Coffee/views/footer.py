import reflex as rx
from Jacaranda_Coffee.styles.colors import Color
from Jacaranda_Coffee.styles.styles import Size
from Jacaranda_Coffee.components.link_icon import link_icon_footer



def footer() -> rx.Component:
    return rx.hstack(
                rx.tablet_and_desktop(
                rx.image(
                    src="coffee_footer.png",
                    alt="Imagen de un vaso de café animado con un texto",
                    width="9em",
                    padding="1em",
                    align_items="center"
                )
                ),
                rx.spacer(),
                rx.spacer(),
                    rx.hstack(
                    link_icon_footer(
                        "instagram",
                        "https://www.instagram.com"                        
                    ),
                    link_icon_footer(
                        "twitter",
                        "https://www.twitter.com"
                    ),
                    link_icon_footer(
                        "twitch",
                        "https://www.facebook.com"
                    )
                    ),
                    rx.spacer(),
                    rx.link(
                        "©Pagina creada por Franco Martínez - Reflex | Python",
                        href="https://hermes.reflex.run/",
                        is_external=True,
                        margin="1em",
                        color="#828282"
                        ),
                bg=Color.TERTIARY.value,
                width="100%",
                height="auto",
                align="center",
            )
               
