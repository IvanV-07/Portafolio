import reflex as rx
from portafolio.components.icon_badge import icon_badge
from portafolio.components.icon_button import icon_button
from portafolio.data import Info
from portafolio.styles.styles import IMAGE_HEIGHT, EmSize, Size


def info_detail(info: Info, colored_icon: bool = False) -> rx.Component:
    body_children = [
        rx.text.strong(info.title),
        rx.text(info.subtitle),
        rx.text(
            info.description,
            size=Size.SMALL.value,
            color_scheme="gray",
        ),
    ]

    if info.technologies:
        body_children.append(
            rx.flex(
                *[
                    rx.badge(
                        rx.box(class_name=technology.icon),
                        technology.name,
                        color_scheme="gray",
                    )
                    for technology in info.technologies
                ],
                wrap="wrap",
                spacing=Size.SMALL.value,
            )
        )

    link_buttons = []
    if info.url:
        link_buttons.append(icon_button("link", info.url))
    if info.github:
        link_buttons.append(icon_button("github", info.github))
    if link_buttons:
        body_children.append(rx.hstack(*link_buttons))

    side_children = []
    if info.date:
        side_children.append(rx.badge(info.date))
    if info.certificate:
        side_children.append(
            icon_button("shield-check", info.certificate, solid=True)
        )

    flex_children = [
        rx.hstack(
            icon_badge(info.icon, colored=colored_icon),
            rx.vstack(
                *body_children,
                spacing=Size.SMALL.value,
                width="100%",
            ),
            spacing=Size.DEFAULT.value,
            width="100%",
        ),
    ]
    if info.image:
        flex_children.append(
            rx.image(
                src=info.image,
                height=IMAGE_HEIGHT,
                width="auto",
                border_radius=EmSize.DEFAULT.value,
                object_fit="cover",
            )
        )
    if side_children:
        flex_children.append(
            rx.vstack(
                *side_children,
                spacing=Size.SMALL.value,
                align="end",
            )
        )

    return rx.flex(
        *flex_children,
        flex_direction=["column-reverse", "row"],
        spacing=Size.DEFAULT.value,
        width="100%",
    )
