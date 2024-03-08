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
                rx.text("Honguini", as_="span", color=Color.PRIMARY.value),
                rx.text("Productions", as_="span", color=Color.SECONDARY.value),
                style=styles.navbar_title_style
                ),
            href=""
            ),
        ),
        rx.spacer(),
        rx.link(
            "Productos",
            href="",
        ),
        rx.link(
            "Mision",
            href="",
        ),
        rx.link(
            "contactanos",
            href="",
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"
    )
   