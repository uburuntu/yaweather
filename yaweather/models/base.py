from enum import Enum, IntEnum, auto

from pydantic import BaseConfig, BaseModel, Extra


class Base(BaseModel):
    class Config(BaseConfig):
        extra = Extra.allow
        use_enum_values = True


class MoonCode(IntEnum):
    full_moon = 0
    waning_crescent_1 = auto()
    waning_crescent_2 = auto()
    waning_crescent_3 = auto()
    last_quarter = auto()
    waning_gibbous_1 = auto()
    waning_gibbous_2 = auto()
    waning_gibbous_3 = auto()
    new_moon = auto()
    waxing_gibbous_1 = auto()
    waxing_gibbous_2 = auto()
    waxing_gibbous_3 = auto()
    first_quarter = auto()
    waxing_crescent_1 = auto()
    waxing_crescent_2 = auto()
    waxing_crescent_3 = auto()


class MoonText(str, Enum):
    full_moon = 'moon-code-0'
    waning_crescent_1 = 'moon-code-1'
    waning_crescent_2 = 'moon-code-2'
    waning_crescent_3 = 'moon-code-3'
    last_quarter = 'moon-code-4'
    waning_gibbous_1 = 'moon-code-5'
    waning_gibbous_2 = 'moon-code-6'
    waning_gibbous_3 = 'moon-code-7'
    new_moon = 'moon-code-8'
    waxing_gibbous_1 = 'moon-code-9'
    waxing_gibbous_2 = 'moon-code-10'
    waxing_gibbous_3 = 'moon-code-11'
    first_quarter = 'moon-code-12'
    waxing_crescent_1 = 'moon-code-13'
    waxing_crescent_2 = 'moon-code-14'
    waxing_crescent_3 = 'moon-code-15'


class Condition(str, Enum):
    clear = 'clear'
    partly_cloudy = 'partly-cloudy'
    cloudy = 'cloudy'
    overcast = 'overcast'
    drizzle = 'drizzle'
    light_rain = 'light-rain'
    rain = 'rain'
    moderate_rain = 'moderate-rain'
    heavy_rain = 'heavy-rain'
    continuous_heavy_rain = 'continuous-heavy-rain'
    showers = 'showers'
    wet_snow = 'wet-snow'
    light_snow = 'light-snow'
    snow = 'snow'
    snow_showers = 'snow-showers'
    hail = 'hail'
    thunderstorm = 'thunderstorm'
    thunderstorm_with_rain = 'thunderstorm-with-rain'
    thunderstorm_with_hail = 'thunderstorm-with-hail'


class PhenomCondition(str, Enum):
    fog = 'fog'
    mist = 'mist'
    smoke = 'smoke'
    dust = 'dust'
    dust_suspension = 'dust-suspension'
    duststorm = 'duststorm'
    thunderstorm = 'thunderstorm'
    drifting_snow = 'drifting-snow'
    blowing_snow = 'blowing-snow'
    ice_pellets = 'ice-pellets'
    freezing_rain = 'freezing-rain'
    tornado = 'tornado'
    volcanic_ash = 'volcanic-ash'


class DayTime(str, Enum):
    # Light time of day
    d = 'd'
    # Dark time of day
    n = 'n'


class WindDir(str, Enum):
    # Northwest
    nw = 'nw'
    # North
    n = 'n'
    # Northeast
    ne = 'ne'
    # East
    e = 'e'
    # Southeast
    se = 'se'
    # South
    s = 's'
    # Southwest
    sw = 'sw'
    # West
    w = 'w'
    # Calm
    c = 'c'


class PrecipitationType(IntEnum):
    no_precipitation = 0
    rain = 1
    sleet = 2
    snow = 3
    hail = 4


class Season(str, Enum):
    summer = 'summer'
    autumn = 'autumn'
    winter = 'winter'
    spring = 'spring'


class Lang(str, Enum):
    # Russian for the Russia locale
    ru_RU = 'ru_RU'
    # Russian for the Ukraine locale
    ru_UA = 'ru_UA'
    # Ukrainian for the Ukraine locale
    uk_UA = 'uk_UA'
    # Belarusian for the Belarus locale
    be_BY = 'be_BY'
    # Kazakh for the Kazakhstan locale
    kk_KZ = 'kk_KZ'
    # Turkish for the Turkey locale
    tr_TR = 'tr_TR'
    # International English
    en_US = 'en_US'
