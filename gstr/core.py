from dataclasses import dataclass
from typing import Literal, Optional

from .caps import GstBaseCaps
from .element import GstElement

__all__ = ['CapsFilter', 'FakeSink', 'FileSink', 'FileSrc', 'Queue', 'Tee']


@dataclass
class CapsFilter(GstElement):
    caps: GstBaseCaps


@dataclass
class FakeSink(GstElement): ...


@dataclass
class FileSink(GstElement):
    location: str


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
