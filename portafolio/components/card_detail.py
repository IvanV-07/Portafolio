import reflex as rx
from portafolio.data import Extra

from portafolio.styles.styles import EmSize, IMAGE_HEIGHT, Size


def card_detail(extra: Extra) -> rx.Component:
    return rx.card(
        rx.inset(
            rx.image(
                src=extra.image,
                height=IMAGE_HEIGHT,
                width="100%",
                object_fit="cover"
            ),
            pb=Size.MEDIUM.value
        ),
        rx.text.strong(extra.title, margin_top=EmSize.DEFAULT.value),
        rx.text(
            extra.description,
            size=Size.SMALL.value,
            color_scheme="gray"
        ),
        width="100%"
    )
