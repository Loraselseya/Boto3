import boto3

client = boto3.client("ec2")

# Create VPC
#client.create_vpc(CidrBlock='10.0.0.0/24')


# Describe VPC
import boto3
x=client.describe_vpcs()
#print(x)
no_of_vpcs=x["Vpcs"]

for vpc in no_of_vpcs:
    print(vpc["VpcId"])


# Listing security group

x=client.describe_security_groups()
no_of_security_grp=len(x["SecurityGroups"])
print(no_of_security_grp)

for group in x["SecurityGroups"]:
    print(group["GroupId"])


# Describe security group

x=client.describe_security_groups(
    Filters=[
        {
            'Name': 'group-id',
            'Values': [
                'sg-045c04b94e7a4f7cb'
            ]
        },
    ],
)

print(x) 


