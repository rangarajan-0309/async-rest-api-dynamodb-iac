# Async REST API with DynamoDB and AWS CDK
Architecture:
Client
  |
  v
API Gateway (with Basic Auth via Lambda Authorizer)
  |
  v
FastAPI (Lambda) ---> Amazon SQS ---> Lambda Worker ---> DynamoDB

## Features
- FastAPI with Basic Auth
- Async processing via SQS
- Data stored in DynamoDB
- Deployed with AWS CDK
- Unit tested with pytest

## Usage
```bash
cd iac
cdk deploy
```

## Test
```bash
pytest tests/
```

## Deploy
- Configure AWS credentials.
- Deploy using AWS CDK.
![Alt text](<API Gateway.png>)

Included Modules:
app/main.py: FastAPI app with Basic Authentication and SQS integration.

lambda/worker.py: Lambda function to consume messages and store to DynamoDB.

iac/: AWS CDK (Python) stack to deploy API Gateway, Lambda, SQS, and DynamoDB.

tests/test_api.py: Unit tests for authentication and SQS integration using pytest.

requirements.txt: Required libraries.

README.md: Project overview, deploy instructions, and usage.