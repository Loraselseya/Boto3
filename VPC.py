import boto3

client = boto3.client("ec2")

# Create VPC
client.create_vpc(CidrBlock='10.0.0.0/24')

# Describe VPC
import boto3
x=client.describe_vpcs()
#print(x)

no_of_vpcs=x["Vpcs"]

for vpc in no_of_vpcs:
    print(vpc["VpcId"])
