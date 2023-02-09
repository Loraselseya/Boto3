# List IAM Users

import boto3

AWS_REGION = "ap-south-1"

# Create IAM client
iam = boto3.client('iam', region_name= AWS_REGION)

# List users with the pagination interface
paginator = iam.get_paginator('list_users')
for response in paginator.paginate():
    print(response)

