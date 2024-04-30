import reflex as rx
from Jacaranda_Coffee.components.title import method_title
from Jacaranda_Coffee.styles.styles import Size, TextColor, Color

def mas_info(text:str, text1:str, text2:str, text3:str, image:str, alt:str) ->rx.Component:
    return rx.dialog.root(
                rx.dialog.trigger(
                    rx.chakra.button(
                            "+ info", 
                            margin_left=Size.SMALL.value,
                            style={
                                "background":Color.PRIMARY.value,
                                "color":Color.CUARTIARY.value,
                                "width":"80px"
                            },
                            _hover={
                                "background": Color.SECONDARY.value,
                                "color": TextColor.PRIMARY.value
                            }, 
                        ),),
                rx.dialog.content(
                    rx.dialog.title(method_title(text)),
                    rx.dialog.description(
                        text1,
                        style={
                            'text_indent':"1em"
                        }                    
                    ),
                    rx.dialog.description(
                        text2,
                        style={
                            'text_indent':"1em"
                        }                
                    ),
                    rx.dialog.description(
                        text3,
                        style={
                            'text_indent':"1em",
                        }                
                    ),
                    rx.chakra.center( 
                        rx.chakra.image(
                            src=image,
                            alt=alt,
                            width="140px",
                            height="auto",
                            padding=Size.SMALL.value
                        )   
                    ),             
                    rx.dialog.close(
                        rx.chakra.center(
                            rx.chakra.button(
                                "Cerrar", 
                                margin=Size.SMALL.value,
                                style={
                                    "background":Color.SECONDARY.value,
                                    "color":TextColor.PRIMARY.value,
                                    "width":"80px"
                                },
                                _hover={
                                    "background": Color.ACCENT.value,
                                    "color": TextColor.PRIMARY.value
                                },  
                            ),
                        )
                    ),
                    bg=Color.PRIMARY.value,
                    color=TextColor.PRIMARY.value,
                    border=f"2px solid {TextColor.PRIMARY.value}",
                )
            )
            