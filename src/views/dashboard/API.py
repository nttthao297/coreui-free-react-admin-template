import boto3
import configparser
import collections
collections.Callable = collections.abc.Callable
config = configparser.ConfigParser()
config.read('config.ini')

s3 = boto3.client('s3',
                endpoint_url='https://s3.us-west-1.wasabisys.com',
                  aws_access_key_id=config['default']['aws_access_key_id'],
                  aws_secret_access_key=config['default']['aws_secret_access_key'])

def create_bucket (bucket_name, region):
    config = configparser.ConfigParser()
    config.read('config.ini')
    s3 = boto3.client('s3',
                endpoint_url='https://s3.us-west-1.wasabisys.com',
                  aws_access_key_id=config['default']['aws_access_key_id'],
                  aws_secret_access_key=config['default']['aws_secret_access_key'])
    s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': region})

def put_object(file_path, bucket_name, key_name):
    config = configparser.ConfigParser()
    config.read('config.ini')
    s3 = boto3.client('s3',
                endpoint_url='https://s3.us-west-1.wasabisys.com',
                  aws_access_key_id=config['default']['aws_access_key_id'],
                  aws_secret_access_key=config['default']['aws_secret_access_key'])
    s3.put_object(Body=file_path, Bucket=bucket_name, Key=key_name)

def list_objects(bucket_name, max_keys):
    config = configparser.ConfigParser()
    config.read('config.ini')
    s3 = boto3.client('s3',
                endpoint_url='https://s3.us-west-1.wasabisys.com',
                  aws_access_key_id=config['default']['aws_access_key_id'],
                  aws_secret_access_key=config['default']['aws_secret_access_key'])
    response = s3.list_objects_v2(Bucket=bucket_name, MaxKeys=max_keys)
    contents = response['Contents']
    keys = [item['Key'] for item in contents]
    print(keys)
    

def delete_object(bucket_name, key_name):
    config = configparser.ConfigParser()
    config.read('config.ini')
    s3 = boto3.client('s3',
                endpoint_url='https://s3.us-west-1.wasabisys.com',
                  aws_access_key_id=config['default']['aws_access_key_id'],
                  aws_secret_access_key=config['default']['aws_secret_access_key'])
    s3.delete_object(Bucket=bucket_name, Key=key_name)

create_bucket(bucket_name, region)
put_object(file_path, bucket_name, key_name)
list_objects(bucket_name, 10)
delete_object(bucket_name, key_name)
