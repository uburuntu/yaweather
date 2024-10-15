from typing import Optional

from .base import Base


class TzInfo(Base):
    # Time zone in seconds from UTC
    offset: int
    # Name of the time zone
    name: str
    # Abbreviated name of the time zone
    abbr: Optional[str] = None
    # Daylight saving time
    dst: Optional[bool] = None


class Info(Base):
    # The latitude (in degrees).
    lat: float
    # The longitude (in degrees)
    lon: float
    # Information about the time zone
    tzinfo: Optional[TzInfo] = None
    # The normal pressure for the given coordinates (mm Hg)
    def_pressure_mm: Optional[int] = None
    # The normal pressure for the given coordinates (hPa)
    def_pressure_pa: Optional[int] = None
    # Locality page on Yandex.Weather (https://yandex.ru/pogoda/)
    url: str
