from typing import Any, Optional, Union

from flet_core import AnimationCurve, Axis, Ref, TextStyle
from flet.core.badge import BadgeValue
from flet_core.tooltip import TooltipValue
from flet_core.types import AnimationValue
from flet.core.constrained_control import ConstrainedControl
from flet.core.types import (
    CrossAxisAlignment,
    OffsetValue,
    OptionalControlEventCallable,
    OptionalNumber,
    ResponsiveNumber,
    RotateValue,
    ScaleValue
)


class Marquee(ConstrainedControl):
    def __init__(
        self,
        text: str,
        style: TextStyle = None,
        scroll_axis: Axis = Axis.HORIZONTAL,
        horizontal_alignment: CrossAxisAlignment = CrossAxisAlignment.START,
        blank_space: float = 0.0,
        velocity: float = 50.0,
        pause_after_round: int = 0,
        start_padding: float = 0.0,
        acceleration_duration: int = 0,
        acceleration_curve: AnimationCurve = AnimationCurve.DECELERATE,
        deceleration_duration: int = 0,
        deceleration_curve: AnimationCurve = AnimationCurve.DECELERATE,
        show_fading_only_when_scrolling: bool = True,
        rounds: int = None,
        fading_edge_start_fraction: float = 0.0,
        fading_edge_end_fraction: float = 0.0,
        start_after: int = 0,
        text_scale_factor: float = None,
        on_done = None,
        #
        # ConstrainedControl
        #
        ref: Optional[Ref] = None,
        key: Optional[str] = None,
        width: OptionalNumber = None,
        height: OptionalNumber = None,
        left: OptionalNumber = None,
        top: OptionalNumber = None,
        right: OptionalNumber = None,
        bottom: OptionalNumber = None,
        expand: Union[None, bool, int] = None,
        expand_loose: Optional[bool] = None,
        col: Optional[ResponsiveNumber] = None,
        opacity: OptionalNumber = None,
        rotate: RotateValue = None,
        scale: ScaleValue = None,
        offset: OffsetValue = None,
        aspect_ratio: OptionalNumber = None,
        animate_opacity: Optional[AnimationValue] = None,
        animate_size: Optional[AnimationValue] = None,
        animate_position: Optional[AnimationValue] = None,
        animate_rotation: Optional[AnimationValue] = None,
        animate_scale: Optional[AnimationValue] = None,
        animate_offset: Optional[AnimationValue] = None,
        on_animation_end: OptionalControlEventCallable = None,
        tooltip: TooltipValue = None,
        badge: Optional[BadgeValue] = None,
        visible: Optional[bool] = None,
        disabled: Optional[bool] = None,
        data: Any = None,
        rtl: Optional[bool] = None,
    ):
        ConstrainedControl.__init__(
            self,
            ref=ref,
            key=key,
            width=width,
            height=height,
            left=left,
            top=top,
            right=right,
            bottom=bottom,
            expand=expand,
            expand_loose=expand_loose,
            col=col,
            opacity=opacity,
            rotate=rotate,
            scale=scale,
            offset=offset,
            aspect_ratio=aspect_ratio,
            animate_opacity=animate_opacity,
            animate_size=animate_size,
            animate_position=animate_position,
            animate_rotation=animate_rotation,
            animate_scale=animate_scale,
            animate_offset=animate_offset,
            on_animation_end=on_animation_end,
            tooltip=tooltip,
            badge=badge,
            visible=visible,
            disabled=disabled,
            data=data,
            rtl=rtl,
        )

        self.text = text
        self.style = style
        self.scroll_axis = scroll_axis
        self.horizontal_alignment = horizontal_alignment
        self.blank_space = blank_space
        self.velocity = velocity
        self.pause_after_round = pause_after_round
        self.start_padding = start_padding
        self.acceleration_duration = acceleration_duration
        self.acceleration_curve = acceleration_curve
        self.deceleration_duration = deceleration_duration
        self.deceleration_curve = deceleration_curve

        self.show_fading_only_when_scrolling = show_fading_only_when_scrolling
        self.rounds = rounds
        self.fading_edge_start_fraction = fading_edge_start_fraction
        self.fading_edge_end_fraction = fading_edge_end_fraction
        self.start_after = start_after
        self.text_scale_factor = text_scale_factor
        self.on_done = on_done

    def _get_control_name(self):
        return "marquee"

    @property
    def text(self) -> Optional[str]:
        return self._get_attr("text")
    
    @text.setter
    def text(self, text: Optional[str]):
        self._set_attr("text", text)

    @property
    def style(self) -> Optional[TextStyle]:
        return self._get_attr("style")

    @style.setter
    def style(self, value: Optional[TextStyle]):
        self._set_attr("style", value)

    @property
    def scroll_axis(self) -> Optional[Axis]:
        return self._get_attr("scrollAxis")

    @scroll_axis.setter
    def scroll_axis(self, value: Optional[Axis]):
        self._set_attr("scrollAxis", value)

    @property
    def horizontal_alignment(self) -> Optional[CrossAxisAlignment]:
        return self._get_attr("crossAxisAlignment")

    @horizontal_alignment.setter
    def horizontal_alignment(self, value: Optional[CrossAxisAlignment]):
        self._set_attr("crossAxisAlignment", value)

    @property
    def blank_space(self) -> Optional[float]:
        return self._get_attr("blankSpace")

    @blank_space.setter
    def blank_space(self, value: Optional[float]):
        self._set_attr("blankSpace", value)

    @property
    def velocity(self) -> Optional[float]:
        return self._get_attr("velocity")

    @velocity.setter
    def velocity(self, value: Optional[float]):
        self._set_attr("velocity", value)

    @property
    def pause_after_round(self) -> Optional[int]:
        return self._get_attr("pauseAfterRound")

    @pause_after_round.setter
    def pause_after_round(self, value: Optional[int]):
        self._set_attr("pauseAfterRound", value)

    @property
    def start_padding(self) -> Optional[float]:
        return self._get_attr("startPadding")

    @start_padding.setter
    def start_padding(self, value: Optional[float]):
        self._set_attr("startPadding", value)

    @property
    def acceleration_duration(self) -> Optional[int]:
        return self._get_attr("accelerationDuration")

    @acceleration_duration.setter
    def acceleration_duration(self, value: Optional[int]):
        self._set_attr("accelerationDuration", value)

    @property
    def acceleration_curve(self) -> Optional[AnimationCurve]:
        return self._get_attr("accelerationCurve")

    @acceleration_curve.setter
    def acceleration_curve(self, value: Optional[AnimationCurve]):
        self._set_attr("accelerationCurve", value)

    @property
    def deceleration_duration(self) -> Optional[int]:
        return self._get_attr("decelerationDuration")

    @deceleration_duration.setter
    def deceleration_duration(self, value: Optional[int]):
        self._set_attr("decelerationDuration", value)

    @property
    def deceleration_curve(self) -> Optional[AnimationCurve]:
        return self._get_attr("decelerationCurve")

    @deceleration_curve.setter
    def deceleration_curve(self, value: Optional[AnimationCurve]):
        self._set_attr("decelerationCurve", value)

    @property
    def show_fading_only_when_scrolling(self) -> Optional[bool]:
        return self._get_attr("showFadingOnlyWhenScrolling")

    @show_fading_only_when_scrolling.setter
    def show_fading_only_when_scrolling(self, value: Optional[bool]):
        self._set_attr("showFadingOnlyWhenScrolling", value)

    @property
    def rounds(self) -> Optional[int]:
        return self._get_attr("numberOfRounds")

    @rounds.setter
    def rounds(self, value: Optional[int]):
        self._set_attr("numberOfRounds", value)

    @property
    def fading_edge_start_fraction(self) -> Optional[float]:
        return self._get_attr("fadingEdgeStartFraction")

    @fading_edge_start_fraction.setter
    def fading_edge_start_fraction(self, value: Optional[float]):
        self._set_attr("fadingEdgeStartFraction", value)

    @property
    def fading_edge_end_fraction(self) -> Optional[float]:
        return self._get_attr("fadingEdgeEndFraction")

    @fading_edge_end_fraction.setter
    def fading_edge_end_fraction(self, value: Optional[float]):
        self._set_attr("fadingEdgeEndFraction", value)

    @property
    def start_after(self) -> Optional[int]:
        return self._get_attr("startAfter")

    @start_after.setter
    def start_after(self, value: Optional[int]):
        self._set_attr("startAfter", value)

    @property
    def text_scale_factor(self) -> Optional[float]:
        return self._get_attr("textScaleFactor")

    @text_scale_factor.setter
    def text_scale_factor(self, value: Optional[float]):
        self._set_attr("textScaleFactor", value)

    # on_done
    @property
    def on_done(self) -> OptionalControlEventCallable:
        return self._get_event_handler("done")

    @on_done.setter
    def on_done(self, handler: OptionalControlEventCallable):
        self._add_event_handler("done", handler)
        self._set_attr("onDone", True if handler is not None else None)
