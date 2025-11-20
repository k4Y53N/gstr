from dataclasses import dataclass
from typing import Literal

from .element import GstElement

__all__ = [
    'RTSPSrc',
    'RTSPClientSink',
]


@dataclass
class RTSPSrc(GstElement):
    location: str
    protocols: Literal['tcp', 'udp', 'udp-mcast' 'tcp+udp-mcast+udp'] | None = None


@dataclass
class RTSPClientSink(GstElement):
    location: str
    protocols: Literal['tcp', 'udp', 'udp-mcast' 'tcp+udp-mcast+udp'] | None = None
