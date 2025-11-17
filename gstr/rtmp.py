from dataclasses import dataclass

from .element import GstElement

__all__ = [
    'RTMPSrc',
    'RTMPSink',
    'RTMP2Src',
    'RTMP2Sink',
]


@dataclass
class RTMPSrc(GstElement):
    location: str


@dataclass
class RTMPSink(GstElement):
    location: str


@dataclass
class RTMP2Src(GstElement):
    location: str


@dataclass
class RTMP2Sink(GstElement):
    location: str
