from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Link:
    name: str
    url: str


@dataclass
class Body:
    text: str
    link: Optional[Link]


@dataclass
class Message:
    title: str
    subtitle: Optional[List[str]]
    body: Body
