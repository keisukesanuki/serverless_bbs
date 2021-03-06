import json
import boto3
import time
import datetime
import uuid
import os
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):

    responseHeaders = {
      "Access-Control-Allow-Methods": "OPTIONS,GET,POST",
      "Access-Control-Allow-Headers" : "*",
      "Access-Control-Allow-Origin": "*"
    }

    print(event['body'])
    req = json.loads(event['body'])

    item = {
        'postId': str(uuid.uuid4()),
        'date': str(datetime.datetime.now()),
        'owner': req['owner'],
        'note': req['note'],
        'enable': bool('True')
    }

    table = _get_database().Table('bbs')

    res = table.put_item(Item=item)

    return {
        "headers": responseHeaders,
        "statusCode": 200,
        "body": item,
    }

def _get_database():
    endpoint = boto3.resource('dynamodb', endpoint_url=os.environ["DYNAMO_ENDPOINT"])
    return endpoint
