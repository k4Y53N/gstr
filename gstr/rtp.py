from dataclasses import dataclass

from .element import GstElement

__all__ = [
    'RTPH264Pay',
    'RTPH264Depay',
]


@dataclass
class RTPH264Pay(GstElement): ...


@dataclass
class RTPH264Depay(GstElement): ...
