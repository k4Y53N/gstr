from dataclasses import dataclass

from .element import GstElement

__all__ = [
    'RTPH264Depay',
]


@dataclass
class RTPH264Depay(GstElement): ...
