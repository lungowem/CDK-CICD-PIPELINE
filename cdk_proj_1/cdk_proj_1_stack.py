from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_iam as iam,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
    aws_s3 as s3,
    aws_ec2 as ec2,
    aws_cloudwatch as cloudwatch,
)


class CdkProj1Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, "My-cdk-bucket-1lulu")

        # queue = sqs.Queue(
        #     self, "CdkProj1Queue",
        #     visibility_timeout=Duration.seconds(300),
        # )

        # topic = sns.Topic(
        #     self, "CdkProj1Topic"
        # )

        # topic.add_subscription(subs.SqsSubscription(queue))
