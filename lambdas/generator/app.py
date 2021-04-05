import requests
import os
import json

def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):
    endpoint = os.environ['QUEUE_PROXY_ENDPOINT']
    response = requests.post(endpoint, json = {'eventId':'1337'})
    return respond(None, res='SUCCESS')