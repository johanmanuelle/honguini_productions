import reflex as rx
from honguini_productions.styles.styles import Size, Spacing
from honguini_productions.styles.colors import Color, TextColor
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/images/Honguini-01.png",
            height=Size.VERY_BIG.value,
            width=Size.VERY_BIG.value,
            alt="Logotipo de Honguni Productions. Una \"eme\" entre llaves."
        ),
        rx.link(
            rx.box(
                f"© 2020-{datetime.date.today().year} ",
                rx.text(
                    "Honguini Productions",
                    as_="span",
                    color=Color.PRIMARY.value
                ),
                " v1.",
                padding_top=Size.DEFAULT.value
            ),
            href="",
            is_external=False,
            font_size=Size.MEDIUM.value
        ),
        rx.link(
            rx.hstack(
                rx.image(
                    src="/icons/icons8-planet-50.png",
                    height=Size.LARGE.value,
                    width=Size.LARGE.value
                ),
                rx.text(
                    "ESTAMOS COMPROMETIDOS CON EL CUIDADO DEL PLANETA!.",
                    font_size=Size.MEDIUM.value,
                    margin_top=Size.ZERO.value
                ),
            ),
            href="",
            is_external=False
        ),

        align="center",
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.VERY_BIG.value,
        padding_x=Size.BIG.value,
        spacing=Spacing.ZERO.value,
        color=TextColor.FOOTER.value
    )