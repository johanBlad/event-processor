import boto3
import json
import os

region_name = os.environ['REGION_NAME']
dynamo = boto3.client('dynamodb', region_name=region_name)
table_name = os.environ['TABLE_NAME']

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    records = [r['body'] for r in event['Records']]
    for record in records:
        print(record)
        write_result = dynamo.put_item(TableName=table_name, Item={'eventId': {'S': str(record['eventId'])}})
        print(write_result)
    return "SUCCESS"
