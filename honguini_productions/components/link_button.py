import reflex as rx
import honguini_productions.styles.styles as styles
from honguini_productions.styles.styles import Size, Color, Spacing


def link_button(title: str,
                body: str,
                image: str,
                url: str,
                is_external=True,
                highlight_color=None,
                animated=False) -> rx.Component:

    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=Size.LARGE.value,
                    height=Size.LARGE.value,
                    margin=Size.MEDIUM.value,
                    alt=title
                ),
                rx.vstack(
                    rx.text(
                        title,
                        size=Spacing.SMALL.value,
                        style=styles.button_title_style
                    ),
                    rx.text(
                        body,
                        size=Spacing.VERY_SMALL.value,
                        style=styles.button_body_style
                    ),
                    align_items="start",
                    spacing=Spacing.VERY_SMALL.value,
                    padding_y=Size.SMALL.value,
                    padding_right=Size.SMALL.value
                ),
                align="center",
                width="100%"
            ),
            border=f"{'2px' if highlight_color != None else '0px'} solid {highlight_color}",
            class_name=styles.BOUNCEIN_ANIMATION if animated else None
        ),
        href=url,
        is_external=is_external,
        width="100%"
    )
