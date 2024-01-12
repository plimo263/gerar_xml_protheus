from dataclasses import dataclass
from datetime import date
from typing import List


@dataclass
class XMLDBFilter:

    CFOP: List[str] = None
    CHV: List[str] = None
    DATE_FROM: date = None
    DATE_TO: date  = None
    NUM_DOC: List[str] = None
