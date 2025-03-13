from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass
from typing import Any, Dict, List, Optional

__all__ = ['RawElement', 'GstElement']


class Element(ABC):
    """Abstract base class for all elements."""

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
        """Connect two elements in series.

        Args:
            other (Element): The other element to connect.

        Returns:
            Element: The current element.
        """
        if self.sinks:
            self.sinks[-1].__or__(other)
        else:
            self.sinks.append(other)
            other.srcs.append(self)

        return self

    def __mul__(self, other: 'Element') -> 'Element':
        """Connect two elements in parallel.

        Args:
            other (Element): The other element to connect.

        Returns:
            Element: The current element.
        """
        self.sinks.append(other)
        other.srcs.append(self)

        return self

    @abstractmethod
    def get_properties(self) -> Dict[str, Any]:
        """Get the properties of the element.

        Returns:
            Dict[str, Any]: The properties of the element.
        """

    def build(self, other: Optional['Element'] = None) -> str:
        """Build the element.

        Args:
            other (Optional[Element], optional): Element to skip build. Defaults to None.

        Returns:
            str: The built element.
        """
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

            src_element = None

            if len(src.sinks) > 1:
                src_element = f'{src.build(self)} {src.name}.'
            else:
                src_element = src.build(self)

            if len_srcs > 1:
                links.append(f'{src_element} ! {self.name}.')
            else:
                links.append(f'{src_element} ! {element}')
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
        """Get the element type.

        Returns:
            str: The element type.
        """
        return self.__class__.__name__.lower()

    @property
    def name(self) -> Optional[str]:
        """Get the name of the element.

        Returns:
            Optional[str]: The name of the element.
        """
        return self.__class__.__name__.upper()

    @property
    def srcs(self) -> List['Element']:
        """Get the sources of the element.

        Returns:
            List[Element]: The sources of the element.
        """
        if self.__srcs is None:
            self.__srcs = []

        return self.__srcs

    @property
    def sinks(self) -> List['Element']:
        """Get the sinks of the element.

        Returns:
            List[Element]: The sinks of the element.
        """
        if self.__sinks is None:
            self.__sinks = []

        return self.__sinks

    def build_properties(self, with_name=False) -> List[str]:
        """Build the properties of the element.

        Args:
            with_name (bool, optional): Add name property. Defaults to False.

        Returns:
            List[str]: The properties of the element.
        """
        properties = self.get_properties()

        if with_name:
            properties['name'] = self.name

        return [
            f'{self.clean_property_key(k)}={self.clean_property_value(v)}'
            for k, v in properties.items()
            if v is not None
        ]

    def separate(self) -> str:
        """Get the separator for the element.

        Returns:
            str: The separator for the element.
        """
        return ' '

    def clean_property_key(self, key: str) -> str:
        """Clean the property key. If the key starts with an underscore, it will be removed. All underscores will be replaced with hyphens.

        Args:
            key (str): The property key.

        Returns:
            str: The cleaned property key.
        """
        if key.startswith('_'):
            key = key[1:]

        return str(key).replace('_', '-')

    def clean_property_value(self, value: Any) -> str:
        """Clean the property value. If the value is a boolean, it will be converted to a string.

        Args:
            value (Any): The property value.

        Returns:
            str: The cleaned property value.
        """
        if isinstance(value, bool):
            return str(value).lower()

        return str(value)


class RawElement(Element):
    def __init__(self, E: str, **kwargs):
        self.E = E
        self.properties = kwargs

    def T(self) -> str:
        return self.E

    @property
    def name(self):
        return self.E.upper()

    def get_properties(self) -> Dict[str, Any]:
        return self.properties


@dataclass
class GstElement(Element):
    def get_properties(self) -> Dict[str, Any]:
        return asdict(self)
