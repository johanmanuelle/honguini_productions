import reflex as rx
import honguini_productions.constants as const
import honguini_productions.styles.styles as styles
from honguini_productions.routes import Route
from honguini_productions.components.link_button import link_button
from honguini_productions.components.title import title
from honguini_productions.styles.styles import Color, Spacing



def index_links() -> rx.Component:
    return rx.vstack(
        title("Lo Que Ofrecemos"),
        link_button(
            "Nuestros Productos",
            "Mira los productos hechos con impresion 3D que tenemos en Stock",
            "/icons/icons8-products-50.png",
            Route.PRODUCTS.value,
            False,
            Color.SECONDARY.value
        ),
        
        #link_button(
        #    "Mision",
        #    "Que soluciones queremos ofrecer por medio de nuestros productos?",
        #    "/icons/icons8-mission-50.png",
        #    const.FACEBOOK_URL
        #),
        
        title("Contacto"),
        link_button(
            "Whatsapp",
            "Respuesta rápida y con preferencia",
            "/icons/icons8-whatsapp.svg",
            const.WHATSAPP_URL
        ),
        link_button(
            "Email",
            const.EMAIL,
            "/icons/email.svg",
            f"mailto:{const.EMAIL}"
        ),
        width="100%",
        spacing=Spacing.DEFAULT.value,
        
    )
