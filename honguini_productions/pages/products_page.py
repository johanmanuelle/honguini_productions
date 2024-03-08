import reflex as rx
import honguini_productions.utils as utils
import honguini_productions.styles.styles as styles
from honguini_productions.routes import Route
from honguini_productions.components.navbar import navbar
from honguini_productions.components.footer import footer
from honguini_productions.views.header import header
from honguini_productions.styles.styles import Size
from honguini_productions.views.products_view import products_views


@rx.page(
    route=Route.PRODUCTS.value,
    title=utils.products_title,
    description=utils.products_description,
    image=utils.preview,
    meta=utils.products_meta
)
def products_page() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                #header(),
                #courses_links(),
                #sponsors(),
                products_views(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )
