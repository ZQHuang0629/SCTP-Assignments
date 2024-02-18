import boto3

# Create a new S3 client
s3_client = boto3.client('s3')

# Define the name of the bucket to be created
bucket_name = 'zhangqin-s3-assignment'

# Specify the region for the bucket (optional, if not specified, it will use the default region from AWS configuration)
bucket_region = 'ap-southeast-1'

# Create the S3 bucket
try:
    response = s3_client.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': bucket_region
        }
    )
    print("Bucket created successfully!")
except Exception as e:
    print("Error creating bucket:", e)
