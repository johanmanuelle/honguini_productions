import reflex as rx
from honguini_productions.styles.styles import Size

def products (image: str, url: str, alt: str) -> rx.Component:
    return rx.image(
        src=image,
        width=Size.ULTRA_INSTINCT.value,
        height=Size.ULTRA_INSTINCT.value,
        alt=alt
    )