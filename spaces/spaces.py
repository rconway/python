import boto3
from botocore.client import Config

# Initialize a session using DigitalOcean Spaces.
session = boto3.session.Session()
client = session.client('s3',
                        region_name='ams3',
                        endpoint_url='https://ams3.digitaloceanspaces.com',
                        aws_access_key_id='TBD',
                        aws_secret_access_key='tbd')

# Create a new Space.
client.create_bucket(Bucket='rac-my-new-space')

# List all buckets on your account.
response = client.list_buckets()
spaces = [space['Name'] for space in response['Buckets']]
print("Spaces List: %s" % spaces)