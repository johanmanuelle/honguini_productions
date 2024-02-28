import reflex as rx

config = rx.Config(
    app_name="honguini_productions",
    api_url="https://honguiniproductions.com:8000",
     cors_allowed_origins=[
        "http://localhost:3000",
        "https://honguiniproductions.com"
    ]
)