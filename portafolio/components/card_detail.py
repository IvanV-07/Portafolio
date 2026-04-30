import reflex as rx
from portafolio.data import Extra

from portafolio.styles.styles import EmSize, IMAGE_HEIGHT, Size


def card_detail(extra: Extra) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.image(
                src=extra.image,
                height=IMAGE_HEIGHT,
                width="100%",
                object_fit="cover",
                border_radius=EmSize.DEFAULT.value,
            ),
            rx.text.strong(extra.title),
            rx.text(
                extra.description,
                size=Size.SMALL.value,
                color_scheme="gray",
            ),
            spacing=Size.DEFAULT.value,
            width="100%",
        ),
        width="100%",
    )
