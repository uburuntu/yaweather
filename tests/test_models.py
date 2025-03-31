import json
from pathlib import Path

import pytest

from yaweather import ResponseForecast


def load_responses():
    responses = []

    for dump in (Path(__file__).parent / 'resources').iterdir():
        if dump.name.startswith('responses') and dump.suffix == '.json':
            curr_responses = json.loads(dump.read_text(encoding='utf-8'))
            responses.append(curr_responses)

    return responses


class TestModels:
    @pytest.mark.parametrize('responses', load_responses())
    def test_response_parsing(self, responses):
        for response in responses:
            ResponseForecast.model_validate(response)
