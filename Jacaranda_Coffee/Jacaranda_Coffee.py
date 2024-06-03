import reflex as rx
import Jacaranda_Coffee.styles.styles as styles
from Jacaranda_Coffee.views.navbar import navbar
from Jacaranda_Coffee.views.header import header_with_image_and_text
from Jacaranda_Coffee.views.info import info
from Jacaranda_Coffee.views.contact import contact_form
from Jacaranda_Coffee.views.metodos import metods
from Jacaranda_Coffee.views.footer import footer
from Jacaranda_Coffee.views.speciality_coffee import speciality_coffee
from Jacaranda_Coffee.components.green_line import green_line
from Jacaranda_Coffee.views.carrusel import home_carousel


def index() -> rx.Component:
    return rx.box(
        navbar(),
        #header_with_image_and_text(),
        home_carousel(),
        speciality_coffee(),
        info(),
        metods(),
        green_line(),
        contact_form(),
        green_line(),
        footer()
    )
    
app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
)

app.add_page(
    index,
    title="Jacaranda Coffee | Café de especialidad",
    description="Cafetería de especialidad en España"
)
