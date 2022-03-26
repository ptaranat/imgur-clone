import json
from backend.list_s3_objects import list_obj


def test_list_obj():
    event = ""
    context = ""
    result = list_obj(event, context)
    assert result["statusCode"] == 200
    assert isinstance(json.loads(result["body"]), list)
