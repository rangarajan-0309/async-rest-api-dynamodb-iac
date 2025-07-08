import boto3, json, os

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.getenv("DYNAMODB_TABLE"))

def lambda_handler(event, context):
    for record in event['Records']:
        body = json.loads(record['body'])
        table.put_item(Item=body)
    return {"status": "processed"}