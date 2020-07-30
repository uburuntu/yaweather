from typing import Optional

from .base import Base, Condition, DayTime, PhenomCondition, PrecipitationType, Season, WindDir


class Fact(Base):
    # Temperature (°C)
    temp: float
    # What the temperature feels like (°C)
    feels_like: float
    # The water temperature (°C). This parameter is returned for localities where this information is relevant
    temp_water: Optional[float]
    # The code of the weather icon.
    icon: str
    # The code for the weather description
    condition: Condition
    # Wind speed (meters per second)
    wind_speed: float
    # Speed of wind gusts (meters per second)
    wind_gust: float
    # Wind direction
    wind_dir: WindDir
    # Atmospheric pressure (mm Hg)
    pressure_mm: int
    # Atmospheric pressure (hPa)
    pressure_pa: int
    # Humidity (percent)
    humidity: float
    # Light or dark time of the day
    daytime: DayTime
    # Indicates that the time of day specified in the daytime field is polar
    polar: bool
    # Time of year in this locality
    season: Season
    # The time when weather data was measured, in Unix time
    obs_time: int
    # Indicates a thunderstorm
    is_thunder: Optional[bool]
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
    # The code for an additional weather event icon
    phenom_icon: Optional[str]
    # The code for an additional weather description
    phenom_condition: Optional[PhenomCondition]

    @property
    def icon_url(self) -> Optional[str]:
        return self.icon and f'https://yastatic.net/weather/i/icons/blueye/color/svg/{self.icon}.svg'

    @property
    def phenom_icon_url(self) -> Optional[str]:
        return self.phenom_icon and f'https://yastatic.net/weather/i/icons/blueye/color/svg/{self.phenom_icon}.svg'
