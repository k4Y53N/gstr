from dataclasses import dataclass
from typing import Literal

from .element import GstElement

__all__ = [
    'Queue',
    'Tee',
    'FileSrc',
    'FileSink',
]


@dataclass
class Queue(GstElement):
    leaky: Literal['no', 'upstream', 'downstream'] | None = None


@dataclass
class Tee(GstElement): ...


@dataclass
class FileSrc(GstElement):
    location: str


@dataclass
class FileSink(GstElement):
    location: str
