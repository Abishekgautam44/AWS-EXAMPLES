import logging
import boto3
from botocore.exceptions import ClientError

# def create_bucket(bucket_name, region="us-west-2"):
#     """Create an S3 bucket in a specified region."""
#     try:
#         s3_client = boto3.client('s3', region_name=region)
#         s3_client.create_bucket(
#             Bucket=bucket_name,
#             CreateBucketConfiguration={'LocationConstraint': region}
#         )
#         print(f"Bucket '{bucket_name}' created successfully.")
#     except ClientError as e:
#         logging.error(e)
#         return False
#     return True

#Initialize S3 resource
s3 = boto3.resource('s3')

# Create a new bucket
bucket_name = "max-demo-abi"
# create_bucket(bucket_name)

# Print all S3 buckets
print("Buckets in your account:")
for bucket in s3.buckets.all():
    print(bucket.name)

def delete_bucket(bucket_name):
    """Delete an s3 bucket"""
    try:
        s3_client = boto3.client('s3')
        s3_client.delete_bucket(Bucket=bucket_name);
        print(f"Bucket '{bucket_name}' deleted successfully.")
    except ClientError as e:
        logging.error(e)
        return False
    return

delete_bucket(bucket_name);