from dataclasses import dataclass
from typing import Literal, Optional

from .caps import GstBaseCaps
from .element import GstElement

__all__ = ['CapsFilter', 'FileSrc', 'Queue', 'Tee']


@dataclass
class CapsFilter(GstElement):
    caps: GstBaseCaps


@dataclass
class FileSrc(GstElement):
    location: str


@dataclass
class Queue(GstElement):
    leaky: Optional[
        Literal[
            'no',
            'upstream',
            'downstream',
        ]
    ] = None


@dataclass
class Tee(GstElement): ...
