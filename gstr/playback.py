from dataclasses import dataclass

from .element import GstElement

__all__ = [
    'DecodeBin',
    'URIDecodeBin',
]


@dataclass
class DecodeBin(GstElement): ...


@dataclass
class URIDecodeBin(GstElement):
    uri: str
