from dataclasses import dataclass
from typing import Optional

from .element import GstElement

__all__ = ['VideoRate']


@dataclass
class VideoRate(GstElement):
    average_period: Optional[int] = None
    drop: Optional[bool] = None
    drop_only: Optional[bool] = None
    drop_out_of_segment: Optional[bool] = None
    duplicate: Optional[int] = None
    _in: Optional[int] = None
    max_closing_segment_duplication_duration: Optional[int] = None
    max_duplication_time: Optional[int] = None
    max_rate: Optional[int] = None
    new_pref: Optional[int] = None
    out: Optional[int] = None
    rate: Optional[int] = None
    silent: Optional[bool] = None
    skip_to_first: Optional[bool] = None
