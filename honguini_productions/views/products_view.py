import reflex as rx
from honguini_productions.components.products import products
from honguini_productions.styles.styles import Spacing
from honguini_productions.components.title import title

def products_views () -> rx.Component:
    return rx.vstack(
         title("Soportes PS4 FAT/Slim/Pro"),
            products(
                "/images/ps4-3.webp",
                "https://www.honguiniproductions.com",
                "Imagen Frontal Ps4 con Soportes"

            ),
            products(
                "/images/ps4-4.webp",
                "https://www.honguiniproductions.com",
                "Imagen Lateral Ps4 con soportes instalados"
            ),
            products(
                "/images/ps4-1.jpg",
                "https://www.honguiniproductions.com",
                "Imagen del soporte del PS4"
            ),
            products(
                "/images/ps4-2.jpg",
                "https://www.honguiniproductions.com",
                "Muestra Imagen Soporte Ps4"
            ),

            title("$33.000 COP Envio Gratis Toda Colombia"),
            width="100%",
            spacing=Spacing.DEFAULT.value
                               

    )