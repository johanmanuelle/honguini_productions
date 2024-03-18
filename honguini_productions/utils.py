import reflex as rx

# Común


def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")


preview = "https://honguiniproductions.com/preview.png"

_meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:image", "content": preview},
    
]

# Index

index_title = "Honguini Productions| Tu sitio de Impresión 3D y Costura de Confianza"
index_description = "Ofrecemos una amplia gama de productos en impresion 3D y costura, no dudes en contactarnos!."

index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]
index_meta.extend(_meta)

# Productos

products_title = "Honguini Productions| Nuestros Productos"
products_description = "aqui puedes ver nuestra gama de productos hechos en impresión 3D y costura"

products_meta = [
    {"name": "og:title", "content": products_title},
    {"name": "og:description", "content": products_description},
]
products_meta.extend(_meta)