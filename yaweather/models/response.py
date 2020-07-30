import datetime
from typing import List

from .base import Base
from .fact import Fact
from .forecast import Forecast
from .info import Info


class Response(Base):
    pass


class ResponseForecast(Response):
    now: int
    now_dt: datetime.datetime
    info: Info
    fact: Fact
    forecasts: List[Forecast]
