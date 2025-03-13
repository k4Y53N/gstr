from dataclasses import dataclass

from .element import GstElement

__all__ = ['DecodeBin', 'UriDecodeBin']


@dataclass
class DecodeBin(GstElement): ...


@dataclass
class UriDecodeBin(GstElement):
    uri: str
