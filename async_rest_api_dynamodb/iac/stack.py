from aws_cdk import (
    Stack, aws_lambda as lambda_, aws_apigateway as apigw,
    aws_sqs as sqs, aws_dynamodb as ddb
)
from constructs import Construct

class DataApiStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        queue = sqs.Queue(self, "DataQueue")

        table = ddb.Table(self, "DataTable",
            partition_key={"name": "id", "type": ddb.AttributeType.STRING}
        )

        api_lambda = lambda_.Function(self, "ApiHandler",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="main.handler",
            code=lambda_.Code.from_asset("app"),
            environment={
                "SQS_QUEUE_URL": queue.queue_url,
                "BASIC_AUTH_USERNAME": "admin",
                "BASIC_AUTH_PASSWORD": "secret"
            }
        )

        worker_lambda = lambda_.Function(self, "WorkerHandler",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="worker.lambda_handler",
            code=lambda_.Code.from_asset("lambda"),
            environment={"DYNAMODB_TABLE": table.table_name}
        )

        queue.grant_send_messages(api_lambda)
        queue.grant_consume_messages(worker_lambda)
        table.grant_write_data(worker_lambda)

        apigw.LambdaRestApi(self, "Endpoint", handler=api_lambda)
