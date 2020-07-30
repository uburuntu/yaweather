from typing import Optional

from pydantic import PositiveInt

from .base import Base, Lang


class Request(Base):
    def prepare(self) -> dict:
        d = self.dict(exclude_none=True)
        for k, v in d.items():
            if isinstance(v, (bool, float)):
                d[k] = str(v)
        return d


class RequestForecast(Request):
    # The latitude in degrees
    lat: float
    # The longitude in degrees
    lon: float
    # The combination of language and country that weather information will be returned for
    lang: Optional[Lang]
    # The number of days in the forecast, including the current day
    limit: Optional[PositiveInt]
    # For each day, the response will contain the hourly weather forecast
    hours: Optional[bool]
    # Extra information about precipitation
    extra: Optional[bool]
