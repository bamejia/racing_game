import json


def get_json(obj):
    """ Turns an object and its attributes into a JSON string """
    return json.loads(
        json.dumps(obj, default=lambda o: getattr(o, '__dict__', str(o)))
    )
