from aws_cdk import (
    Stack,
    aws_sns as sns,
)
from constructs import Construct

class CdkDemo1Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create the SNS topic
        cdktest_topic = sns.Topic(self, 'CdkTestTopic', topic_name='cdktest')