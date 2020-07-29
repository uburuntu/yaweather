import datetime
from typing import List

from ..models.base import Base
from ..models.fact import Fact
from ..models.forecast import Forecast
from ..models.info import Info


class Response(Base):
    pass


class ResponseForecast(Response):
    now: int
    now_dt: datetime.datetime
    info: Info
    fact: Fact
    forecasts: List[Forecast]
