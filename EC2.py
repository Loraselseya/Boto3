# Create EC2
import boto3

ec2_resource=boto3.resource("ec2")

ec2_resource.create_instances(
    ImageId='ami-01a4f99c4ac11b03c',
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1
)


# Listing EC2

AWS_REGION = "ap-south-1"
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)

instances = EC2_RESOURCE.instances.all()

for instance in instances:
    print("EC2 instance",{instance.id})


# Terminate EC2

AWS_REGION = "ap-south-1"
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
INSTANCE_ID = 'i-00b9e99ce4f55b55e'

instance = EC2_RESOURCE.Instance(INSTANCE_ID)

instance.terminate()

print(f'Terminating EC2 instance: {instance.id}')