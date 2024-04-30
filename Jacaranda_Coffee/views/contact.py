import reflex as rx
from Jacaranda_Coffee.styles.colors import TextColor, Color
from Jacaranda_Coffee.components.title import title
from Jacaranda_Coffee.styles.styles import Size

class ContactFormState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Manejar el envío del formulario."""
        self.form_data = form_data

def contact_form():
    return rx.form(
        rx.vstack(
            title("Contáctanos")
        ),
        rx.box(
        rx.vstack(
            rx.input(
                placeholder="First Name",
                name="first_name",
                required=True,
                style={
                    "width": ["20em","40em"], 
                    "height": "3.3em", 
                    "background": Color.CUARTIARY.value,   
                },                 
            ),
            rx.input(
                placeholder="Last Name",
                name="last_name",
                required=True,
                style={
                    "width": ["20em","40em"], 
                    "height": "3.3em", 
                    "background": Color.CUARTIARY.value,   
                }, 
            ),
            rx.input(
                placeholder="Número de Teléfono (Opcional)",
                name="phone_number",
                required=False,
                style={
                    "width": ["20em","40em"], 
                    "height": "3.3em", 
                    "background": Color.CUARTIARY.value,   
                },  
            ),
            rx.input(
                placeholder="Correo Electrónico",
                name="email",
                required=True,
                type="email",
                style={
                    "width": ["20em","40em"], 
                    "height": "3.3em", 
                    "background": Color.CUARTIARY.value,
                },  
            ),

            rx.button(
                "Enviar", 
                type="submit", 
                bg=Color.PRIMARY.value, 
                width="5em", 
                height="3.3em",
                margin_top=Size.DEFAULT.value,
                _hover={
                    "background": Color.SECONDARY.value,
                    "color": TextColor.PRIMARY.value
                },
                ),
                padding=Size.BIG.value,
                spacing="2",
                width="100%"
            )
        ),
                on_submit=ContactFormState.handle_submit,
                reset_on_submit=True,
                background="center/cover url('/bg_contact.jpg')"
    )
    
    
