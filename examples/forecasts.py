from yaweather import UnitedStates, YaWeather

y = YaWeather(api_key='secret')

res = y.forecast(UnitedStates.NewYork)

for f in res.forecasts:
    day = f.parts.day_short
    print(f'{f.date} | {day.temp} °C, {day.condition}')
