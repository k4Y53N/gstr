from dataclasses import dataclass

from .element import GstElement

__all__ = [
    'DecodeBin',
    'DecodeBin3',
    'URIDecodeBin',
    'URIDecodeBin3',
]


@dataclass
class DecodeBin(GstElement): ...


@dataclass
class DecodeBin3(GstElement): ...


@dataclass
class URIDecodeBin(GstElement):
    uri: str


@dataclass
class URIDecodeBin3(GstElement):
    uri: str
