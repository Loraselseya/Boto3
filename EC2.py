import boto3

ec2_resource=boto3.resource("ec2")

ec2_resource.create_instances(
    ImageId='ami-01a4f99c4ac11b03c',
    InstanceType='t2.micro',
)