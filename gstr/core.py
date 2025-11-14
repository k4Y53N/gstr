from dataclasses import dataclass
from typing import Literal

from .element import GstElement

__all__ = [
    'Queue',
    'Tee',
]


@dataclass
class Queue(GstElement):
    leaky: Literal['no', 'upstream', 'downstream'] = 'no'


@dataclass
class Tee(GstElement): ...
