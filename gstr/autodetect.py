from dataclasses import dataclass

from .element import GstElement

__all__ = [
    'AutoVideoSink',
]


@dataclass
class AutoVideoSink(GstElement): ...
