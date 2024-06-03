import reflex as rx
from Jacaranda_Coffee.styles.styles import Size
from Jacaranda_Coffee.styles.fonts import Font
from Jacaranda_Coffee.styles.colors import Color, TextColor

class Slick(rx.Component):
    """Slick slider component for main page carousel."""

    library = "react-slick@0.21.0"
    tag = "Slider"

    dots: bool = False
    arrows: bool = False
    infinite: bool = True
    speed: int = 500
    autoplay: bool = True
    autoplaySpeed: int = 4000
    lazyload: bool = True
    is_default = True
    slides_to_show: int = 1
    slides_to_scroll: int = 1
    initial_slide: int = 2
    pause_on_hover: bool = False

    lib_dependencies: list[str] = ["slick-carousel@1.8.1"]

    def _get_custom_code(self) -> str | None:
        return """
        import "slick-carousel/slick/slick.css";
        import "slick-carousel/slick/slick-theme.css";
        """


slick = Slick.create


def development_card() -> rx.Component:
    return rx.heading(
        rx.hstack(
        rx.box(
            rx.text(
                "¿Quieres unirte a la verdadera", 
                align="left", 
                size="8",                 
                weight="light",
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
                weight="light",
                as_="div"
            ),
            rx.chakra.button(
                    rx.icon(tag="phone", padding_right="0.5em"),
                    "Escribinos",
                    color=Color.TERTIARY.value,
                    bg=Color.CUARTIARY.value,
                    size="md",
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
                height=["25em","30em"],
                padding_x=["1em","3em"],
                padding_y=["5.5em","10em"],
                top="0"
        ),

        ),
        size="4",
        #width="100%",
    )

def development_card1() -> rx.Component:
    return rx.heading(
        rx.hstack(
        rx.box(
            rx.text(
                "Conoce todo sobre el café...", 
                align="left", 
                size="8",                 
                weight="light",
                as_="div"
            ),
            rx.text(
                " Y sobre nosotros",  
                align="left", 
                size="8",                 
                weight="light",
                as_="div"
            ),
            rx.chakra.button(
                    rx.icon(tag="phone", padding_right="0.5em"),
                    "Escribinos",
                    color=Color.TERTIARY.value,
                    bg=Color.CUARTIARY.value,
                    size="md",
                    margin_top=Size.MEDIUM.value,
                    on_click=rx.redirect(path="/"),
                    is_external=True,
                    _hover={
                        "background": Color.PRIMARY.value,
                        "color": TextColor.PRIMARY.value
                        }
                        ),
                bg="center/cover url('/bg_contact.jpg')",
                spacing="4",
                width="100%",
                height=["25em","30em"],
                padding_x=["1em","3em"],
                padding_y=["8em","10em"],
                top="0"
        ),
        ),
        size="4",
        #width="100%",
    )


"""class ClickState(rx.State):
    cursor = "grab"

    def change_cursor(self):
        if self.cursor == "grabbing":
            self.cursor = "grab"
        else:
            self.cursor = "grabbing"""


def home_carousel() -> rx.Component:
    return rx.heading(
        slick(
            development_card(),
            development_card1(),
        ),
        #on_mouse_down=ClickState.change_cursor,
        #on_mouse_up=ClickState.change_cursor,
        width="full",
    )
