from dataclasses import dataclass

from .element import GstElement

__all__ = [
    'RTSPSrc',
]


@dataclass
class RTSPSrc(GstElement):
    uri: str
