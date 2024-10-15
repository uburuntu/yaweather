import datetime
from typing import List, Optional

from pydantic import validator

from .base import Base, Condition, DayTime, MoonCode, MoonText, PrecipitationType, WindDir


class ForecastParts(Base):
    # Nighttime forecast
    night: Optional['Forecast'] = None
    # Morning forecast
    morning: Optional['Forecast'] = None
    # Afternoon forecast
    day: Optional['Forecast'] = None
    # Evening forecast
    evening: Optional['Forecast'] = None
    # 12-hour forecast for the day
    day_short: Optional['Forecast'] = None
    # Nighttime forecast
    night_short: Optional['Forecast'] = None


class Forecast(Base):
    # Date of the forecast, in the format YYYY-MM-DD
    date: Optional[datetime.date] = None
    # The date of the forecast in Unix time
    date_ts: Optional[int] = None
    # Week number
    week: Optional[int] = None
    # Time of the sunrise in local time (may be omitted for polar regions)
    sunrise: Optional[str] = None
    # Time of the sunset in local time (may be omitted for polar regions)
    sunset: Optional[str] = None
    # Code of the lunar phase.
    moon_code: Optional[MoonCode] = None
    # Text code for the lunar phase.
    moon_text: Optional[MoonText] = None
    # Forecasts by time of day and 12-hour forecasts.
    # Contains fields that differ by type of forecast:
    #     Nighttime forecast
    #     Morning forecast
    #     Afternoon forecast
    #     Evening forecast
    #     12-hour forecast for the day
    #     Nighttime forecast
    # All weather forecasts for a certain time of day have the same set of fields
    # All 12-hour forecasts have the same set of fields
    # Note: For the last day returned in the forecast, some of the parts might be missing
    parts: Optional[ForecastParts] = None

    @validator('parts', pre=True)
    def parse_parts(cls, v):
        # Note: sometimes arrives as list
        if isinstance(v, list):
            v = {part['part_name']: part for part in v}
        return v

    # Object with the weather forecast for the night
    # The beginning of the nighttime period corresponds to the beginning of the 24-hour period
    # To specify the upcoming night temperatures, use the object for the nighttime forecast for the next day
    night: Optional[ForecastParts] = None
    # Minimum temperature for the time of day (°C)
    temp_min: Optional[float] = None
    # Maximum temperature for the time of day (°C)
    temp_max: Optional[float] = None
    # Average temperature for the time of day (°C)
    temp_avg: Optional[float] = None
    # What the temperature feels like (°C)
    feels_like: Optional[float] = None
    # The code of the weather icon
    icon: Optional[str] = None

    @property
    def icon_url(self) -> Optional[str]:
        return self.icon and f'https://yastatic.net/weather/i/icons/blueye/color/svg/{self.icon}.svg'

    # The code for the weather description
    condition: Optional[Condition] = None
    # Light or dark time of the day
    daytime: Optional[DayTime] = None
    # Indicates that the time of day specified in the daytime field is polar
    polar: Optional[bool] = None
    # Wind speed (meters per second)
    wind_speed: Optional[float] = None
    # Speed of wind gusts (meters per second)
    wind_gust: Optional[float] = None
    # Wind direction
    wind_dir: Optional[WindDir] = None
    # Atmospheric pressure (mm Hg)
    pressure_mm: Optional[int] = None
    # Atmospheric pressure (hPa)
    pressure_pa: Optional[int] = None
    # Humidity (percent)
    humidity: Optional[float] = None
    # Predicted amount of precipitation (mm)
    prec_mm: Optional[float] = None
    # Predicted duration of precipitation (minutes)
    prec_period: Optional[int] = None
    # Type of precipitation
    prec_type: Optional[PrecipitationType] = None
    # Intensity of precipitation
    # Possible values:
    #    0.00 — No precipitation
    #    0.25 — Light rain or snow
    #    0.50 — Rain or snow
    #    0.75 — Heavy rain or snowfall
    #    1.00 — Heavy downpour or snowstorm
    prec_strength: Optional[float] = None
    # Cloud cover
    # Possible values:
    #    0.00 — Clear
    #    0.25 — Partly cloudy
    #    0.50 — Cloudy
    #    0.75 — Cloudy
    #    1.00 — Overcast
    cloudness: Optional[float] = None
    # Object with a 12-hour forecast for the day
    day_short: Optional[ForecastParts] = None
    # Highest daytime or lowest nighttime temperature (°C)
    temp: Optional[float] = None
    # Object for the hourly forecast
    # Consists of 24 parts (hours) for the first 2-3 days, then an empty string is returned
    hours: Optional[List['Forecast']] = None
    # The hour the forecast is for (0-23) using the local time
    hour: Optional[str] = None
    # The time of the forecast in Unix time
    hour_ts: Optional[float] = None


Forecast.update_forward_refs()
ForecastParts.update_forward_refs()
