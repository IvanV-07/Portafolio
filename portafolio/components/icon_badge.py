import reflex as rx

from portafolio.styles.styles import EmSize


def icon_badge(icon: str, colored: bool = False) -> rx.Component:
    return rx.badge(
        rx.icon(
            icon,
            size=32
        ),
        aspect_ratio="1",
        variant="soft",
        color_scheme="mint" if colored else "gray"
    )
