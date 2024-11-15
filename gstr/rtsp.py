from dataclasses import dataclass

from .element import GstElement

__all__ = ['RTPDec', 'RTSPSrc']


@dataclass
class RTPDec(GstElement):
    def T(self) -> str:
        return 'rtpdec'


@dataclass
class RTSPSrc(GstElement):
    location: str
    user_id: str
    user_pw: str

    def T(self) -> str:
        return 'rtspsrc'
