import asyncio

from yaweather import Russia, YaWeatherAsync


async def main():
    async with YaWeatherAsync(api_key='secret') as y:
        res = await y.forecast(Russia.Moscow)

        print(f'Now: {res.fact.temp} °C, feels like {res.fact.feels_like} °C')
        print(f'Condition: {res.fact.condition}')


asyncio.run(main())
