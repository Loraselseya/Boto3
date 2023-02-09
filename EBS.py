# Create EBS

import boto3

AWS_REGION = "ap-south-1"

ec2_client = boto3.client('ec2', region_name=AWS_REGION)

new_volume = ec2_client.create_volume(
    AvailabilityZone=f'{AWS_REGION}a',
    Encrypted = True,
    Size=10,
    VolumeType='gp2',
    TagSpecifications=[
        {
            'ResourceType': 'volume',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'EBS_volume_1'
                }
            ]
        }
    ]
)

print(f'Created volume ID: {new_volume["VolumeId"]}')

# Describe EBS

import json
from datetime import date, datetime
import boto3

AWS_REGION = "ap-south-1"
EC2_CLIENT = boto3.client('ec2', region_name=AWS_REGION)


# Helper method to serialize datetime fields
def json_datetime_serializer(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))


describe_response = EC2_CLIENT.describe_volumes(
    VolumeIds=[
        'vol-0a11f2736c9234027'
    ]
)

print('Volumes information:')
print(json.dumps(
        describe_response,
        indent=4,
        default=json_datetime_serializer
    )
)


# Attach EBS

import boto3
AWS_REGION = "ap-south-1"
ec2_client = boto3.client('ec2', region_name=AWS_REGION)

ec2_client.attach_volume(
    Device='/dev/sdb',
    InstanceId='i-0d5dd9ab9ea500e2c',
    VolumeId='vol-09348d85a7877cc1d'
)


# Detach EBS

import boto3
AWS_REGION = "ap-south-1"
ec2_client = boto3.client('ec2', region_name=AWS_REGION)


ec2_client.detach_volume(
    InstanceId='i-0d5dd9ab9ea500e2c',
    VolumeId='vol-09348d85a7877cc1d'
)
