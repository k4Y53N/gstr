from dataclasses import dataclass

from .element import GstElement

__all__ = [
    'Rtph264Pay',
    'Rtph264Depay',
]


@dataclass
class Rtph264Pay(GstElement): ...


@dataclass
class Rtph264Depay(GstElement): ...
