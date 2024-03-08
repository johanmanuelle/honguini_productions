
from rxconfig import config
from honguini_productions.components.navbar import navbar
from honguini_productions.views.header import header
from honguini_productions.views.index_links import index_links
from honguini_productions.components.footer import footer
from honguini_productions.styles.styles import Size
import honguini_productions.styles.styles as styles
import reflex as rx




#class State(rx.State): #esto es lo que maneja el backend
#    """The app state."""
@rx.page(title="Honguini Productions",description="Tu servicio de impresion 3D bajo demanda y costura artesanal de confianza",image="favicon.ico")

def index() -> rx.Component:
     return rx.box(
        #utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                index_links(),
                #sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )
    

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    )

app.add_page(index)
