from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass
from typing import Any, Dict, List, Optional

__all__ = ['RawElement', 'GstElement']


class Element(ABC):
    __srcs: Optional[List['Element']] = None
    __sinks: Optional[List['Element']] = None

    def __str__(self) -> str:
        return self.build()

    def __repr__(self):
        with_name = max(len(self.srcs), len(self.sinks)) > 1
        properties = self.build_properties(with_name=with_name)
        element = self.separate().join([self.T(), *properties])

        return element

    def __or__(self, other: 'Element') -> 'Element':
        if self.sinks:
            self.sinks[-1].__or__(other)
        else:
            self.sinks.append(other)
            other.srcs.append(self)

        return self

    def __mul__(self, other: 'Element') -> 'Element':
        self.sinks.append(other)
        other.srcs.append(self)

        return self

    @abstractmethod
    def get_properties(self) -> Dict[str, Any]:
        raise NotImplementedError()

    def build(self, other: Optional['Element'] = None) -> str:
        len_srcs = len(self.srcs)
        len_sinks = len(self.sinks)
        with_name = max(len_srcs, len_sinks) > 1
        element_appeneded = False
        properties = self.build_properties(with_name=with_name)
        element = self.separate().join([self.T(), *properties])
        links: List[str] = []

        for src in self.srcs:
            if src is other:
                continue

            if len_srcs > 1:
                links.append(f'{src.build(self)} ! {self.name}.')
            else:
                links.append(f'{src.build(self)} ! {element}')
                element_appeneded = True

        if not element_appeneded:
            links.append(element)

        for sink in self.sinks:
            if sink is other:
                continue

            if len_sinks > 1:
                links.append(f'{self.name}. ! {sink.build(self)}')
            else:
                links.append(f'! {sink.build(self)}')

        return ' '.join(links)

    def T(self) -> str:
        return self.__class__.__name__.lower()

    @property
    def name(self) -> Optional[str]:
        return self.__class__.__name__.upper()

    @property
    def srcs(self) -> List['Element']:
        if self.__srcs is None:
            self.__srcs = []

        return self.__srcs

    @property
    def sinks(self) -> List['Element']:
        if self.__sinks is None:
            self.__sinks = []

        return self.__sinks

    def build_properties(self, with_name=False) -> List[str]:
        properties = self.get_properties()

        if with_name:
            properties['name'] = self.name

        return [
            f'{self.clean_property_key(k)}={self.clean_property_value(v)}'
            for k, v in properties.items()
            if v is not None
        ]

    def separate(self) -> str:
        return ' '

    def clean_property_key(self, key: str) -> str:
        if key.startswith('_'):
            key = key[1:]

        return str(key).replace('_', '-')

    def clean_property_value(self, value: Any) -> str:
        if isinstance(value, bool):
            return str(value).lower()

        return str(value)


class RawElement(Element):
    def __init__(self, E: str, **kwargs):
        self.E = E
        self.properties = kwargs

    def T(self) -> str:
        return self.E

    def get_properties(self) -> Dict[str, Any]:
        return self.properties


@dataclass
class GstElement(Element):
    def get_properties(self) -> Dict[str, Any]:
        return asdict(self)
