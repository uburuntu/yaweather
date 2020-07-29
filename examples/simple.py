from yaweather import UnitedKingdom, YaWeather

y = YaWeather(api_key='secret')
res = y.forecast(UnitedKingdom.London)

print(f'Now: {res.fact.temp} °C, feels like {res.fact.feels_like} °C')
print(f'Condition: {res.fact.condition}')
