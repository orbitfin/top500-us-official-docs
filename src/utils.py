import re
import boto3

s3_client = boto3.client('s3')


def get_presign_url(bucket_name, key):
    """
    Generate a presigned URL to access an S3 object.

    :param bucket_name: The name of the S3 bucket.
    :param key: The key (path/filename) of the S3 object.
    :return: A presigned URL that allows access to the S3 object for a limited time.
    """
    url = s3_client.generate_presigned_url(
        'get_object',
        Params={
            'Bucket': bucket_name,
            'Key': key
        },
        ExpiresIn=3600  # The URL will expire in 3600 seconds (1 hour).
    )
    return url


def s3_split_path(s3_path):
    """
    Split an S3 path into bucket name and key.

    :param s3_path: The full S3 path.
    :return: A tuple containing the bucket name and the key.
    """
    if not s3_path.startswith('s3://'):
        raise Exception("Invalid s3 path format.")

    s3_path_re = re.compile(r"(s3://[a-zA-Z\-_0-9]+)/(.+)")
    path_group = s3_path_re.search(s3_path).groups()

    bucket_name = path_group[0].replace('s3://', '')
    key = path_group[1]
    return bucket_name, key
