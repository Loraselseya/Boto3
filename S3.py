import boto3
s3 = boto3.client('s3')

#Create s3 bucket
s3.create_bucket(Bucket='github-python-gitlab',
    CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'})


# List of existing bucket
response = s3.list_buckets()
print('Existing buckets:')


# Print the Bucket names
for bucket in response['Buckets']:
  print(f'  {bucket["Name"]}')


# Uploading files in bucket
import boto3
s3 = boto3.resource('s3')
s3.meta.client.upload_file(r"C:\Users\Loramary\Desktop\Python\image\AWS.jpg", "github-python-gitlab", "AWS.jpg")


# Downloading file from bucket
import boto3
s3 = boto3.resource('s3')
s3.meta.client.download_file("github-python-gitlab", "AWS-Certified-Solutions-Architect-Associate_badge.jpg", r"C:\Users\Loramary\Desktop\Python\image\AWS-Certified-Solutions-Architect-Associate_badge.jpg")




