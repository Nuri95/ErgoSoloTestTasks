from dataclasses import dataclass
from datetime import datetime


@dataclass
class CacheObjectInfo:
    rate: float
    date: datetime
