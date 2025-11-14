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
    leaky: Literal['no', 'upstream', 'downstream'] = 'no'


@dataclass
class Tee(GstElement): ...


@dataclass
class FileSrc:
    location: str


@dataclass
class FileSink:
    location: str
