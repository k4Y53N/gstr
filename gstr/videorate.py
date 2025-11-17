from dataclasses import dataclass

from .element import GstElement

__all__ = [
    'VideoRate',
]


@dataclass
class VideoRate(GstElement):
    drop_only: bool | None = None
