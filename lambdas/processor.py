import json
import os

import boto3

from common.http_utils import respond
from common.message import Message

region_name = os.environ["REGION_NAME"]
dynamo = boto3.client("dynamodb", region_name=region_name)
table_name = os.environ["TABLE_NAME"]


def format_record(record):
    formatted = {}
    for key, value in record.items():
        formatted[key] = {"S": str(value)}
    return formatted


def lambda_handler(event, context):
    print("Received records event: " + json.dumps(event, indent=2))
    records = [r["body"] for r in event["Records"]]
    print("Number of records:", len(records))
    for record in records:
        deserialized_record = json.loads(record)
        Message.validate(deserialized_record)
        formatted = format_record(deserialized_record)
        write_result = dynamo.put_item(TableName=table_name, Item=formatted)
        print("Wrote record", record)
    return respond(None, res="SUCCESS")
