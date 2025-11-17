from dataclasses import asdict, dataclass
from fractions import Fraction
from typing import Any

from .element import Element

__all__ = [
    'Caps',
    'RawCaps',
    'GstCaps',
    'RawVideoCaps',
    'RawVideoBGRCaps',
]


def get_numer_denom_str(framerate: float) -> str:
    frac = Fraction(framerate).limit_denominator()
    numer, denom = frac.numerator, frac.denominator

    return f'{numer}/{denom}'


class Caps(Element):
    def separate(self) -> str:
        return ','


@dataclass
class RawCaps(Caps):
    C: str
    properties: dict[str, Any] = None

    def T(self) -> str:
        return self.C

    def get_properties(self):
        return self.properties


@dataclass
class CapsMeta:
    width: int | None = None
    height: int | None = None
    framerate: int | float | str | None = None
    format: str | None = None

    def __post_init__(self):
        if isinstance(self.framerate, (int, float)):
            self.framerate = get_numer_denom_str(self.framerate)


@dataclass
class GstCaps(Caps, CapsMeta):
    def get_properties(self):
        return asdict(self)


@dataclass
class RawVideoCaps(GstCaps):
    def T(self) -> str:
        return 'video/x-raw'


@dataclass
class RawVideoBGRCaps(RawVideoCaps):
    format: str = 'BGR'
