from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import boto3, json, base64
from botocore.exceptions import ClientError
import os

app = FastAPI()
security = HTTPBasic()

SQS_QUEUE_URL = os.getenv("SQS_QUEUE_URL")
sqs_client = boto3.client("sqs")

def verify_credentials(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = os.getenv("BASIC_AUTH_USERNAME")
    correct_password = os.getenv("BASIC_AUTH_PASSWORD")
    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return credentials.username

@app.post("/data")
async def receive_data(payload: dict, username: str = Depends(verify_credentials)):
    try:
        sqs_client.send_message(
            QueueUrl=SQS_QUEUE_URL,
            MessageBody=json.dumps(payload)
        )
        return {"status": "queued"}
    except ClientError as e:
        raise HTTPException(status_code=500, detail=str(e))
