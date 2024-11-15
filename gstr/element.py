from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass
from typing import Any, Dict, List, Optional

__all__ = ['RawElement', 'GstElement']


class Element(ABC):
    """Abstract base class for elements in the pipeline.

    Attributes:
        link (BaseElement): The next element in the pipeline.
    """

    link: 'Element' = None
    name: Optional[str] = None
    srcs: Optional[List['Element']] = None
    sinks: Optional[List['Element']] = None

    def T(self) -> str:
        """Return the element type.

        Raises:
            NotImplementedError: Not implemented.

        Returns:
            str: The element type.
        """
        return self.__class__.__name__.lower()

    @abstractmethod
    def get_properties(self) -> Dict[str, Any]:
        """Return the element properties.

        Raises:
            NotImplementedError: Not implemented.

        Returns:
            Dict[str, Any]: The element properties.
        """
        raise NotImplementedError()

    def __str__(self) -> str:
        return self.build()

    def __or__(self, other: 'Element') -> 'Element':
        """Link the current element to another element.

        Args:
            other (BaseElement): The element to link to.

        Returns:
            BaseElement: The current element.
        """
        if self.link is None:
            self.link = other
        else:
            self.link.__or__(other)

        return self

    def get_srcs(self) -> List['Element']:
        """Return the element sources."""
        if self.srcs is None:
            self.srcs = []

        return self.srcs

    def get_sinks(self) -> List['Element']:
        """Return the element sinks."""
        if self.sinks is None:
            self.sinks = []

        return self.sinks

    def get_name(self) -> str:
        """Return the element name."""
        if self.name is not None:
            return self.name

        return self.T().upper()

    def set_name(self, name: str) -> 'Element':
        """Set the element name.

        Args:
            name (str): The element name.

        Returns:
            BaseElement: The current element.
        """
        self.name = name

        return self

    def build(self) -> str:
        """Build the element string representation.

        Returns:
            str: The element string representation.
        """
        properties = self.build_properties()
        element = self.separate().join([self.T(), *properties])

        if self.link is None:
            return element

        return f'{element} ! {self.link}'

    def build_properties(self) -> List[str]:
        """Build the element properties string representation.

        Returns:
            List[str]: The list of properties strings.
        """
        properties = self.get_properties()

        return [
            f'{self.clean_property_key(k)}={self.clean_property_value(v)}'
            for k, v in properties.items()
            if v is not None
        ]

    def separate(self) -> str:
        """Return the separator for the element properties.

        Returns:
            str: The separator.
        """
        return ' '

    def clean_property_key(self, key: str) -> str:
        """Clean the property key.

        Args:
            key (str): The property key.

        Returns:
            str: The cleaned property key.
        """
        if key.startswith('_'):
            key = key[1:]

        return str(key).replace('_', '-')

    def clean_property_value(self, value: Any) -> str:
        """Clean the property value.

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
        """Create a new raw element.

        Args:
            E (str): The element type.
            **kwargs: The element properties
        """
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
