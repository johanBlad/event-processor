import requests
import os
import json
from datetime import datetime
import random

import aiohttp
import asyncio

def respond(err, res=None):
    return {
        "statusCode": "400" if err else "200",
        "body": err.message if err else json.dumps(res),
        "headers": {
            "Content-Type": "application/json",
        },
    }


def generate_payload():
    return json.dumps({"key": f"value-{random.randint(1,9)}"})


async def call(session, url, payload):
    try:
        async with session.post(
            url,
        ) as response:
            read = await response.read()
            status = response.status
            print(datetime.now(), status, payload)
    except aiohttp.client_exceptions.ClientConnectorError as e:
        print(f"Error fetching [{url}]:", e)


async def generate_calls(n):
    async with aiohttp.ClientSession() as session:
        ret = await asyncio.gather(
            *[
                call(session, "http://httpbin.org/post", generate_payload())
                for i in range(n)
            ]
        )
        print(f"Made {len(ret)} calls")
        return ret


def main_local():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(generate_calls(2))


if __name__ == "__main__":
    main_local()


def lambda_handler(event, context):
    endpoint = os.environ["QUEUE_PROXY_ENDPOINT"]
    response = requests.post(endpoint, json={"eventId": "1337"})
    return respond(None, res="SUCCESS")
