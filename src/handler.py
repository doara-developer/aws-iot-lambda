import json


def lambda_handler(event: dict, context):
    print(json.dumps(event))
