from dataclasses import dataclass
from typing import Literal

from .element import GstElement

__all__ = [
    'H264Parse',
    'AVDEC_H264',
    'X264Enc',
    'RTPH264Depay',
]


@dataclass
class H264Parse(GstElement): ...


@dataclass
class AVDEC_H264(GstElement): ...


@dataclass
class X264Enc(GstElement):
    bitrate: int | None = None
    key_int_max: int | None = None
    speed_preset: (
        Literal[
            'None',
            'ultrafast',
            'superfast',
            'veryfast',
            'faster',
            'fast',
            'medium',
            'slow',
            'slower',
            'veryslow',
            'placebo',
        ]
        | None
    ) = None
    tune: Literal['stillimage', 'fastdecode', 'zerolatency'] | None = None


@dataclass
class RTPH264Depay(GstElement): ...
