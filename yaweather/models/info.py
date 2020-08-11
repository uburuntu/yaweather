from typing import Optional

from .base import Base


class TzInfo(Base):
    # Time zone in seconds from UTC
    offset: int
    # Name of the time zone
    name: str
    # Abbreviated name of the time zone
    abbr: Optional[str]
    # Daylight saving time
    dst: Optional[bool]


class Info(Base):
    # The latitude (in degrees).
    lat: float
    # The longitude (in degrees)
    lon: float
    # Information about the time zone
    tzinfo: TzInfo
    # The normal pressure for the given coordinates (mm Hg)
    def_pressure_mm: int
    # The normal pressure for the given coordinates (hPa)
    def_pressure_pa: int
    # Locality page on Yandex.Weather (https://yandex.ru/pogoda/)
    url: str
