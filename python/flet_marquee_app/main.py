import flet as ft
from flet_marquee import Marquee


def main(page: ft.Page):
    marquee = Marquee(
        text="This is a scrolling text in Flet!",
        # style={"fontWeight": "bold"},
        scroll_axis="horizontal",
        horizontal_alignment="start",
        blank_space=20.0,
        velocity=100.0,
        pause_after_round=1000,
        start_padding=10.0,
        acceleration_duration=1000,
        acceleration_curve="linear",
        deceleration_duration=500,
        deceleration_curve="easeOut"
    )
    page.add(marquee)

ft.app(target=main)
