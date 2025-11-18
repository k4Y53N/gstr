from dataclasses import dataclass

from .element import GstElement

__all__ = [
    'FLVMux',
    'FLVDemux',
]


@dataclass
class FLVMux(GstElement): ...


@dataclass
class FLVDemux(GstElement): ...
