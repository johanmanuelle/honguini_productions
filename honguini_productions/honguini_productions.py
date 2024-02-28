"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx

docs_url = ""
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    return rx.center(
        #rx.theme_panel(),
        
        rx.vstack(
            rx.heading("Bienvenido a Honguini Productions!", size="9"),
            rx.text("algo supremamante fest esta por venir, asi que cuidao! "),
            rx.button(
                "Danos una espera!",
                on_click=lambda: rx.redirect(docs_url),
                size="4",
            ),
            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
    )
#<Theme appearance="dark" accentColor="yellow" panelBackground="solid" radius="large">
#<Theme appearance="dark" accentColor="yellow" radius="large">
app = rx.App(
    theme=rx.theme(
        appearance="dark",
        has_background=True,
        panelBackground="solid",
        radius="large",
        accent_color="yellow",
    )
)
app.add_page(index)
