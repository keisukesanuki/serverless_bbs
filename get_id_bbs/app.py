import json
import boto3
import time
import os
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):

    id = event['queryStringParameters']['postId']

    table = _get_database().Table('bbs')

    res = table.query(
        KeyConditionExpression=Key('postId').eq(id)
    )

    items = res['Items']
    return {
        "statusCode": 200,
        "body": items[0] if items else None,
    }

def _get_database():
    endpoint = boto3.resource('dynamodb', endpoint_url=os.environ["DYNAMO_ENDPOINT"])
    return endpoint
