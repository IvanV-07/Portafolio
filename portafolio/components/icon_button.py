import reflex as rx


BRAND_ICON_CLASSES = {
    "github": "devicon-github-original",
    "linkedin": "devicon-linkedin-plain",
}


def icon_button(icon: str, url: str, text="", solid=False) -> rx.Component:
    if icon in BRAND_ICON_CLASSES:
        icon_component = rx.box(
            class_name=BRAND_ICON_CLASSES[icon],
            font_size="20px",
        )
    else:
        icon_component = rx.icon(icon)
    return rx.link(
        rx.button(
            icon_component,
            text,
            variant="solid" if solid else "surface",
        ),
        href=url,
        is_external=True,
    )
