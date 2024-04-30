import reflex as rx
from enum import Enum
from .fonts import Font
from .colors import Color, TextColor

class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "1em"
    DEFAULT = "1.25em"
    BIG = "2em"
    METHOD_TITLE="2.5em"
    TITLE= "4em"
    BUTTON = "3em"
    VERY_BIG = "4em"


STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap",
    "https://fonts.googleapis.com/css2?family=Acme&family=Lilita+One&display=swap"
]

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "color": TextColor.PRIMARY.value,
    "background": Color.ACCENT.value,
}

title_style = dict(
    width="100%",
    font_size=[Size.METHOD_TITLE.value, Size.TITLE.value],
    font_family=Font.TITLE.value,
    color=TextColor.TERTIARY.value,
    spacing="4"
    )

method_title_style = dict(
    width="100%",
    font_size=[Size.BIG.value,Size.METHOD_TITLE.value],
    font_family=Font.TITLE.value,
    color=TextColor.PRIMARY.value,
    )