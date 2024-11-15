from dataclasses import dataclass
from fractions import Fraction
from typing import Any, Dict, Optional

from .element import GstElement

__all__ = ['GstBaseCaps', 'RawGstCaps', 'RawVideoCaps', 'RawVideoBGRCaps']


def get_numer_denom_str(framerate: float) -> str:
    frac = Fraction(framerate).limit_denominator()
    numer, denom = frac.numerator, frac.denominator

    return f'{numer}/{denom}'


@dataclass
class GstBaseCaps(GstElement):
    format: Optional[str] = None
    framerate: Optional[float] = None
    width: Optional[int] = None
    height: Optional[int] = None

    def __post_init__(self) -> None:
        if self.framerate is not None:
            self.framerate = get_numer_denom_str(self.framerate)

    def __str__(self) -> str:
        return f"'{super().__str__()}'"

    def separate(self) -> str:
        return ','


class RawGstCaps(GstBaseCaps):
    def __init__(self, C: str, framerate: Optional[float] = None, **kwargs) -> None:
        self.C = C
        self.properties = kwargs

        if framerate is not None:
            self.properties['framerate'] = get_numer_denom_str(framerate)

    def T(self) -> str:
        return self.C

    def get_properties(self) -> Dict[str, Any]:
        return self.properties

    def separate(self) -> str:
        return ','


@dataclass
class RawVideoCaps(GstBaseCaps):
    def T(self) -> str:
        return 'video/x-raw'


@dataclass
class RawVideoBGRCaps(RawVideoCaps):
    format: str = 'BGR'
