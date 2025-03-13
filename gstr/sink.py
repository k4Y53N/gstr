from dataclasses import dataclass
from typing import Optional

from .element import GstElement

__all__ = ['FakeSink', 'AutoVideoSink', 'FileSink']


@dataclass
class GstBaseSink(GstElement):
    sync: Optional[bool] = None


@dataclass
class FakeSink(GstBaseSink): ...


@dataclass
class AutoVideoSink(GstBaseSink): ...


@dataclass
class FileSink(GstBaseSink):
    location: str
