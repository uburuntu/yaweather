import datetime
from typing import List

from yaweather.models.base import Base
from yaweather.models.fact import Fact
from yaweather.models.forecast import Forecast
from yaweather.models.info import Info


class Response(Base):
    pass


class ResponseForecast(Response):
    now: int
    now_dt: datetime.datetime
    info: Info
    fact: Fact
    forecasts: List[Forecast]
