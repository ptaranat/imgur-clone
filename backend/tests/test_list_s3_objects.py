import pytest
import json
from backend.list_s3_objects import list_obj


def test_list_obj():
    event = ""
    context = ""
    result = list_obj(event, context)
    if result["statusCode"] != 200:
        raise AssertionError
    if not isinstance(json.loads(result["body"]), list):
        raise AssertionError
