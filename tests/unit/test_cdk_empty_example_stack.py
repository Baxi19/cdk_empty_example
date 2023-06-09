import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_empty_example.cdk_empty_example_stack import CdkEmptyExampleStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_empty_example/cdk_empty_example_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkEmptyExampleStack(app, "cdk-empty-example")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
