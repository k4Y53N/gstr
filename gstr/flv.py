from dataclasses import dataclass

from .element import GstElement

__all__ = [
    'FLVMux',
]


@dataclass
class FLVMux(GstElement): ...
