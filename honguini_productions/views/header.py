import reflex as rx
from honguini_productions.styles.colors import Color, TextColor
from honguini_productions.styles.styles import Spacing, Size
from honguini_productions.components.link_icon import link_icon
import honguini_productions.constants as const

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.box(

                rx.avatar(
                    name="Honguini Productions",
                    size=Spacing.MEDIUM_BIG.value,
                    src="images/Honguini-01.png",
                    radius="full",
                    color=TextColor.BODY.value,
                    bg=Color.CONTENT.value,
                    padding="2px",
                    border=f"4px solid {Color.PRIMARY.value}"
                ),
                position="relative"
            ),
            rx.vstack(
                rx.heading(
                    "Honguini Productions",
                    size=Spacing.BIG.value
                ),
                rx.text(
                    "@honguiniproductions",
                    margin_top=Size.ZERO.value,
                    color=Color.PRIMARY.value
                ),
                rx.hstack(

                    link_icon(
                        "/icons/instagram.svg",
                        const.INSTAGRAM_URL,
                        "Instagram"
                    ),
                    link_icon(
                        "/icons/tiktok.svg",
                        const.TIKTOK_URL,
                        "TikTok"
                    ),
                    spacing=Spacing.LARGE.value,
                    padding_top=Size.SMALL.value
                ),
                spacing=Spacing.ZERO.value,
                align_items="start"
            ),
            align="end",
            spacing=Spacing.DEFAULT.value
        ),
        rx.text(
            f"""
            Somos una empresa dedicada a la impresion 3D bajo demanda, tambien contamos
            con disenhos ya definidos que comercializamos bajo pedido, por otro lado tenemos
            costura artesanal de alta calidad, asi que cuidao!
            """,
            font_size=Size.DEFAULT.value,
            color=TextColor.BODY.value
        ),

        width="100%",
        spacing=Spacing.BIG.value,
        align_items="start",
        
    )