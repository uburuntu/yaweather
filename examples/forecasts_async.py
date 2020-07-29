import asyncio

from yaweather import China, YaWeatherAsync


async def main():
    async with YaWeatherAsync(api_key='secret') as y:
        res = await y.forecast(China.Beijing)

        for f in res.forecasts:
            day = f.parts.day_short
            print(f'{f.date} | {day.temp} °C, {day.condition}')


asyncio.run(main())
