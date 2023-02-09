# Create table
import boto3

AWS_REGION = "ap-south-1"

# Get the service resource.
dynamodb = boto3.resource('dynamodb', region_name= AWS_REGION)

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='Boto3-users',
    KeySchema=[
        {
            'AttributeName': 'username',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'last_name',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'username',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'last_name',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists.
table.wait_until_exists()

# Print out some data about the table.
print(table.item_count)



# Creation - Date and time
table = dynamodb.Table('users')
print(table.creation_date_time)



# Creating new item
table.put_item(
   Item={
        'username': 'john',
        'first_name': 'flake',
        'last_name': 'johnny',
        'age': 24,
        'account_type': 'standard_user',
    }
)



# Getting new item
response = table.get_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    }
)
item = response['Item']
print(item)