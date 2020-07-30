import json
from typing import Tuple

import aiohttp
import requests

from .models import Lang, Request, RequestForecast, ResponseForecast


class YaWeatherAPIError(Exception):
    pass


class YaWeatherBase:
    """
    Docs: https://tech.yandex.com/weather/doc/dg/concepts/forecast-test-docpage/
    Docs RU: https://yandex.ru/dev/weather/doc/dg/concepts/forecast-test-docpage/
    """
    api_url = 'https://api.weather.yandex.ru/v2/'

    def __init__(self,
                 api_key: str,
                 lang: Lang = None,
                 limit: int = None,
                 hours: bool = None,
                 extra: bool = None):
        """
        YaWeather initializer

        :param api_key: Token from https://developer.tech.yandex.ru/services/18/
        :param lang: The combination of language and country that weather information will be returned for, defaults to 'en_US'
        :param limit: The number of days in the forecast, including the current day
        :param hours: For each day, the response will contain the hourly weather forecast, defaults to True
        :param extra: Extra information about precipitation, defaults to False
        """
        self.api_key = api_key
        self.lang = lang or Lang.en_US
        self.limit = limit
        self.hours = hours
        self.extra = extra


class YaWeather(YaWeatherBase):
    @property
    def session(self) -> requests.Session:
        session = getattr(self, '_session', None)
        if session is None:
            session = requests.Session()
            session.headers['X-Yandex-API-Key'] = self.api_key
            setattr(self, '_session', session)
        return session

    def close(self):
        """
        Closes session
        :return: None
        """
        self.session.close()

    def __enter__(self):
        return self

    def __aexit__(self, exc_type, exc_val, exc_tb):
        return self.close()

    def _request(self, endpoint: str, request: Request) -> bytes:
        response = self.session.get(self.api_url + endpoint, params=request.prepare())
        if response.status_code != 200:
            raise YaWeatherAPIError(f'[{response.status_code}] {response.reason}')
        result = response.content
        return result

    def _forecast(
            self, coordinates: Tuple[float, float],
            lang: Lang = None, limit: int = None, hours: bool = None, extra: bool = None
    ) -> bytes:
        request = RequestForecast(
            lat=coordinates[0],
            lon=coordinates[1],
            lang=self.lang if lang is None else lang,
            limit=self.limit if limit is None else limit,
            hours=self.hours if hours is None else hours,
            extra=self.extra if extra is None else extra,
        )
        result = self._request('forecast', request)
        return result

    def forecast_raw(
            self, coordinates: Tuple[float, float],
            lang: Lang = None, limit: int = None, hours: bool = None, extra: bool = None
    ) -> dict:
        """
        Request forecast and return API response as raw dict

        :param coordinates: Tuple of two floats: longitude and latitude
        :param lang: The combination of language and country that weather information will be returned for
        :param limit: The number of days in the forecast, including the current day
        :param hours: For each day, the response will contain the hourly weather forecast
        :param extra: Extra information about precipitation
        :return: dict
        """
        result = self._forecast(coordinates, lang, limit, hours, extra)
        return json.loads(result)

    def forecast(
            self, coordinates: Tuple[float, float],
            lang: Lang = None, limit: int = None, hours: bool = None, extra: bool = None
    ) -> ResponseForecast:
        """
        Request forecast and return API response as instance of ResponseForecast

        :param coordinates: Tuple of two floats: longitude and latitude
        :param lang: The combination of language and country that weather information will be returned for
        :param limit: The number of days in the forecast, including the current day
        :param hours: For each day, the response will contain the hourly weather forecast
        :param extra: Extra information about precipitation
        :return: ResponseForecast
        """
        result = self._forecast(coordinates, lang, limit, hours, extra)
        return ResponseForecast.parse_raw(result)


class YaWeatherAsync(YaWeatherBase):
    @property
    def session(self) -> aiohttp.ClientSession:
        session = getattr(self, '_session', None)
        if session is None:
            session = aiohttp.ClientSession(headers={'X-Yandex-API-Key': self.api_key})
            setattr(self, '_session', session)
        return session

    async def close(self):
        """
        Closes session
        :return: None
        """
        await self.session.close()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        return await self.close()

    async def _request(self, endpoint: str, request: Request) -> bytes:
        async with self.session.get(self.api_url + endpoint, params=request.prepare()) as response:
            if response.status != 200:
                raise YaWeatherAPIError(f'[{response.status}] {response.reason}')
            result = await response.read()
            return result

    async def _forecast(
            self, coordinates: Tuple[float, float],
            lang: Lang = None, limit: int = None, hours: bool = None, extra: bool = None
    ) -> bytes:
        request = RequestForecast(
            lat=coordinates[0],
            lon=coordinates[1],
            lang=self.lang if lang is None else lang,
            limit=self.limit if limit is None else limit,
            hours=self.hours if hours is None else hours,
            extra=self.extra if extra is None else extra,
        )
        result = await self._request('forecast', request)
        return result

    async def forecast_raw(
            self, coordinates: Tuple[float, float],
            lang: Lang = None, limit: int = None, hours: bool = None, extra: bool = None
    ) -> dict:
        """
        Request forecast and return API response as raw dict

        :param coordinates: Tuple of two floats: longitude and latitude
        :param lang: The combination of language and country that weather information will be returned for
        :param limit: The number of days in the forecast, including the current day
        :param hours: For each day, the response will contain the hourly weather forecast
        :param extra: Extra information about precipitation
        :return: dict
        """
        result = await self._forecast(coordinates, lang, limit, hours, extra)
        return json.loads(result)

    async def forecast(
            self, coordinates: Tuple[float, float],
            lang: Lang = None, limit: int = None, hours: bool = None, extra: bool = None
    ) -> ResponseForecast:
        """
        Request forecast and return API response as instance of ResponseForecast

        :param coordinates: Tuple of two floats: longitude and latitude
        :param lang: The combination of language and country that weather information will be returned for
        :param limit: The number of days in the forecast, including the current day
        :param hours: For each day, the response will contain the hourly weather forecast
        :param extra: Extra information about precipitation
        :return: ResponseForecast
        """
        result = await self._forecast(coordinates, lang, limit, hours, extra)
        return ResponseForecast.parse_raw(result)
