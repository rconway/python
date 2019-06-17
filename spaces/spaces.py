import boto3
from botocore.client import Config

# Initialize a session using DigitalOcean Spaces.
session = boto3.session.Session()
client = session.client('s3',
                        region_name='ams3',
                        endpoint_url='https://ams3.digitaloceanspaces.com',
                        aws_access_key_id='K7JKWNXLF53X5K3ZYZS2',
                        aws_secret_access_key='mv9j+V++6uhl3UiSmAwH4ExJnV7MafSxlObXWh00S04')

# Create a new Space.
client.create_bucket(Bucket='rac-my-new-space')

# List all buckets on your account.
response = client.list_buckets()
spaces = [space['Name'] for space in response['Buckets']]
print("Spaces List: %s" % spaces)