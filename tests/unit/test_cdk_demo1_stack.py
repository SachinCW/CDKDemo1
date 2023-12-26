import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_demo1.cdk_demo1_stack import CdkDemo1Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_demo1/cdk_demo1_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkDemo1Stack(app, "cdk-demo1")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
