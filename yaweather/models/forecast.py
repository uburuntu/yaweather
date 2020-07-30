import datetime
from typing import List, Optional

from .base import Base, Condition, DayTime, MoonCode, MoonText, PrecipitationType, WindDir


class ForecastParts(Base):
    # Nighttime forecast
    night: Optional['Forecast']
    # Morning forecast
    morning: Optional['Forecast']
    # Afternoon forecast
    day: Optional['Forecast']
    # Evening forecast
    evening: Optional['Forecast']
    # 12-hour forecast for the day
    day_short: Optional['Forecast']
    # Nighttime forecast
    night_short: Optional['Forecast']


class Forecast(Base):
    # Date of the forecast, in the format YYYY-MM-DD
    date: Optional[datetime.date]
    # The date of the forecast in Unix time
    date_ts: Optional[int]
    # Week number
    week: Optional[int]
    # Time of the sunrise in local time (may be omitted for polar regions)
    sunrise: Optional[str]
    # Time of the sunset in local time (may be omitted for polar regions)
    sunset: Optional[str]
    # Code of the lunar phase.
    moon_code: Optional[MoonCode]
    # Text code for the lunar phase.
    moon_text: Optional[MoonText]
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
    parts: Optional[ForecastParts]
    # Object with the weather forecast for the night
    # The beginning of the nighttime period corresponds to the beginning of the 24-hour period
    # To specify the upcoming night temperatures, use the object for the nighttime forecast for the next day
    night: Optional[ForecastParts]
    # Minimum temperature for the time of day (°C)
    temp_min: Optional[float]
    # Maximum temperature for the time of day (°C)
    temp_max: Optional[float]
    # Average temperature for the time of day (°C)
    temp_avg: Optional[float]
    # What the temperature feels like (°C)
    feels_like: Optional[float]
    # The code of the weather icon
    icon: Optional[str]
    # The code for the weather description
    condition: Optional[Condition]
    # Light or dark time of the day
    daytime: Optional[DayTime]
    # Indicates that the time of day specified in the daytime field is polar
    polar: Optional[bool]
    # Wind speed (meters per second)
    wind_speed: Optional[float]
    # Speed of wind gusts (meters per second)
    wind_gust: Optional[float]
    # Wind direction
    wind_dir: Optional[WindDir]
    # Atmospheric pressure (mm Hg)
    pressure_mm: Optional[int]
    # Atmospheric pressure (hPa)
    pressure_pa: Optional[int]
    # Humidity (percent)
    humidity: Optional[float]
    # Predicted amount of precipitation (mm)
    prec_mm: Optional[int]
    # Predicted duration of precipitation (minutes)
    prec_period: Optional[int]
    # Type of precipitation
    prec_type: Optional[PrecipitationType]
    # Intensity of precipitation
    # Possible values:
    #    0.00 — No precipitation
    #    0.25 — Light rain or snow
    #    0.50 — Rain or snow
    #    0.75 — Heavy rain or snowfall
    #    1.00 — Heavy downpour or snowstorm
    prec_strength: Optional[float]
    # Cloud cover
    # Possible values:
    #    0.00 — Clear
    #    0.25 — Partly cloudy
    #    0.50 — Cloudy
    #    0.75 — Cloudy
    #    1.00 — Overcast
    cloudness: Optional[float]
    # Object with a 12-hour forecast for the day
    day_short: Optional[ForecastParts]
    # Highest daytime or lowest nighttime temperature (°C)
    temp: Optional[float]
    # Object for the hourly forecast
    # Consists of 24 parts (hours) for the first 2-3 days, then an empty string is returned
    # Each part contains the following fields:
    #    hour hour_ts temp feels_like icon condition wind_speed wind_gust wind_dir pressure_mm pressure_pa humidity prec_mm prec_period prec_type prec_strength is_thunder cloudness
    hours: Optional[List[dict]]
    # The hour the forecast is for (0-23) using the local time
    hour: Optional[str]
    # The time of the forecast in Unix time
    hour_ts: Optional[float]

    @property
    def icon_url(self) -> Optional[str]:
        return self.icon and f'https://yastatic.net/weather/i/icons/blueye/color/svg/{self.icon}.svg'


ForecastParts.update_forward_refs()
