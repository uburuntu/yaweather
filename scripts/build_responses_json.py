import asyncio
import json
from pathlib import Path

from yaweather import India, Japan, Lang, Russia, UnitedKingdom, UnitedStates, YaWeatherAsync

api_key = 'SECRET'


async def main():
    async with YaWeatherAsync(api_key, lang=Lang.en_US, limit=7, hours=True, extra=True) as y:

        for country in (India, Japan, Russia, UnitedKingdom, UnitedStates):
            cities = list(country.cities().values())
            coros = [y.forecast_raw(coordinates) for coordinates in cities]

            results = []
            for coro in asyncio.as_completed(coros):
                raw_dict = await coro
                results.append(raw_dict)

            Path(f'responses_{country.name()}.json').write_text(json.dumps(results), encoding='utf-8')


asyncio.run(main())
