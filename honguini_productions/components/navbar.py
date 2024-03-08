import reflex as rx
from honguini_productions.styles.colors import Color
from honguini_productions.styles.styles import Size
import honguini_productions.styles.styles as styles

def navbar()-> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.image(src="/images/Honguini-01.png", width="2em"),
            rx.link(
                rx.box(
                rx.text("Honguini", as_="span", color=Color.ORANGE.value),
                rx.text("Productions", as_="span", color=Color.ORANGE_LIGHT.value),
                style=styles.navbar_title_style
                ),
            href="https://honguiniproductions.com"
            ),
        ),
        rx.spacer(),
        rx.link(
            "Inicio",
            href="/",
        ),
        rx.link(
            "Productos",
            href="/productos",
        ),

        rx.link(
            "Contáctanos",
            href="mailto:info@honguiniproductions.com",
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"
    )
   