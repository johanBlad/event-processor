import asyncio
import json
import os
import random
from datetime import datetime

import aiohttp

from common.http_utils import respond
from common.message import Message


def generate_payload():
    message = Message(key=f"value-{random.randint(1,9)}")
    return json.dumps(message.props)


async def call(session, url, payload, t):
    await asyncio.sleep(t * random.randint(0, 1000) / 1000)
    try:
        async with session.post(url, data=payload) as response:
            await response.read()
            status = response.status
            print(datetime.now(), status, payload, sep="\t")
    except aiohttp.client_exceptions.ClientConnectorError as e:
        print(f"Error fetching [{url}]:", e)


async def generate_calls(url, n, t):
    async with aiohttp.ClientSession(
        headers={"Content-Type": "application/json"}
    ) as session:
        ret = await asyncio.gather(
            *[call(session, url, generate_payload(), t) for i in range(n)]
        )
        print(f"Made {len(ret)} calls")


def lambda_handler(event, context):
    URL = os.environ["QUEUE_PROXY_ENDPOINT"]
    CALLS = int(os.environ["NUM_CALLS"])
    SECONDS = int(os.environ["NUM_SECONDS"])
    loop = asyncio.get_event_loop()
    loop.run_until_complete(generate_calls(URL, CALLS, SECONDS))
    return respond(None, res="SUCCESS")
