import json
import boto3
import time
import os
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):

    req = json.loads(event['body'])

    table = _get_database().Table('bbs')

    res = table.delete_item(
        Key={
            'postId': req['postId']
        },
        ReturnValues='ALL_OLD'
    )

    return {
        "statusCode": 200,
        "body": res,
    }

def _get_database():
    endpoint = boto3.resource('dynamodb', endpoint_url=os.environ["DYNAMO_ENDPOINT"])
    return endpoint
