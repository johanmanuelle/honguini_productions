import honguini_productions.styles.styles as styles
import reflex as rx
from honguini_productions.pages.index import index
from honguini_productions.pages.products_page import products_page




#class State(rx.State): #esto es lo que maneja el backend
#    """The app state."""




app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    )

#app.add_page(index)
#app.add_page(products_page)
