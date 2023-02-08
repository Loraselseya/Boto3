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