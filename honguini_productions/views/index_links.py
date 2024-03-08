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
            "/icons/code.svg",
            Route.PRODUCTS.value,
            False,
            Color.SECONDARY.value
        ),
        link_button(
            "Mision",
            "Que soluciones queremos ofrecer por medio de nuestros productos?",
            "/icons/twitch.svg",
            const.FACEBOOK_URL
        ),
        link_button(
            "Discord",
            "El chat y los grupos de estudio de la comunidad",
            "/icons/discord.svg",
            const.GITHUB_URL
        ),
        link_button(
            "YouTube",
            "Tutoriales sobre desarrollo de software semanales",
            "/icons/youtube.svg",
            const.GITHUB_URL
        ),
        link_button(
            "YouTube | canal secundario",
            "Emisiones en directo destacadas",
            "/icons/youtube.svg",
            const.GITHUB_URL
        ),
        title("Contacto"),
        link_button(
            "Whatsapp",
            "Respuesta rápida y con preferencia",
            "/icons/checkemail.svg",
            const.GITHUB_URL
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
