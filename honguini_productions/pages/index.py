import reflex as rx
import honguini_productions.utils as utils
import honguini_productions.styles.styles as styles
from honguini_productions.components.navbar import navbar
from honguini_productions.components.footer import footer
from honguini_productions.views.header import header
from honguini_productions.styles.styles import Size
from honguini_productions.views.index_links import index_links

@rx.page(
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.index_meta
)


def index() -> rx.Component:
     return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                index_links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )
    
