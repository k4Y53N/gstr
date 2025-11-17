from dataclasses import dataclass
from typing import Literal

from .element import GstElement

__all__ = [
    'RTSPSrc',
]


@dataclass
class RTSPSrc(GstElement):
    location: str
    protocols: Literal['tcp', 'udp', 'udp-mcast' 'tcp+udp-mcast+udp'] | None = None
