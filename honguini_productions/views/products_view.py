import reflex as rx
from honguini_productions.components.products import products
from honguini_productions.styles.styles import Spacing
from honguini_productions.components.title import title

def products_views () -> rx.Component:
    return rx.box(
        rx.hstack(
            title("Soportes PS4 FAT/Slim/Pro"),
            products(
                "/images/ps4-1.jpg",
                "https:/www.prueba.com",
                "Hola Buenax"
            ),
            products(
                "/images/ps4-2.jpg",
                "https:/www.prueba.com",
                "Hola Buenax"
            ),
            title("$20.000 COP")
        ),
        witdh="100%",
        spacing=Spacing.DEFAULT.value
    )