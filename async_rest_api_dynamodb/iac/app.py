import aws_cdk as cdk
from iac.stack import DataApiStack

app = cdk.App()
DataApiStack(app, "DataApiStack")
app.synth()