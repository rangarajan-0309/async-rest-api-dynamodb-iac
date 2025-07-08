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