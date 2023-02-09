# create IAM User

import boto3

# Create IAM client
iam = boto3.client('iam')

# Create user
response = iam.create_user(
    UserName='IAM_USER_NAME'
)

print(response)



# List IAM Users

import boto3

AWS_REGION = "ap-south-1"

# Create IAM client
iam = boto3.client('iam', region_name= AWS_REGION)

# List users with the pagination interface
paginator = iam.get_paginator('list_users')
for response in paginator.paginate():
    print(response)


# Delete IAM User
import boto3

# Create IAM client
iam = boto3.client('iam')

# Delete a user
iam.delete_user(
    UserName='IAM_USER_NAME'
)

