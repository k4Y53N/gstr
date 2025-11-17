from dataclasses import dataclass
from typing import Literal

from .caps import Caps
from .element import GstElement

__all__ = [
    'AppSrc',
    'AppSink',
]


@dataclass
class AppSrc(GstElement):
    block: bool | None = None
    caps: Caps | None = None
    do_timestamp: bool | None = None
    is_live: bool | None = None
    leaky_type: Literal['none', 'upstream', 'downstream'] | None = None


@dataclass
class AppSink(GstElement):
    caps: Caps | None = None
    drop: bool | None = None
    sync: bool | None = None
