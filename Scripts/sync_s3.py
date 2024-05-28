import boto3
import os

def sync_s3(bucket_name, local_dir, s3_dir):
    s3 = boto3.client('s3')
    for root, dirs, files in os.walk(local_dir):
        for file in files:
            local_path = os.path.join(root, file)
            relative_path = os.path.relpath(local_path, local_dir)
            s3_path = os.path.join(s3_dir, relative_path)
            s3.upload_file(local_path, bucket_name, s3_path)

if __name__ == "__main__":
    bucket_name = "your-bucket-name"
    local_dir = "path/to/local/dir"
    s3_dir = "path/to/s3/dir"
    sync_s3(bucket_name, local_dir, s3_dir)
