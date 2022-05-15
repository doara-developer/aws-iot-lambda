import json


def lambda_handler(event: dict, context):
    json.dumps(event)
