from typing import List, Dict
from fastapi import FastAPI
#from fs import open_fs
import s3fs
import boto3
import configparser
import collections
import os
import io
import tempfile
import subprocess
import time
import webbrowser
# collections.Callable = collections.abc.Callable
config = configparser.ConfigParser()
config.read('./config.ini')
aws_access_key_id = "LFBEPMDW9N4M2A2IMF5H"
aws_secret_access_key = "Yuh4hWYQAejLjUM5rJsHXAODZbiNRcoCdRC1oB0C"

app = FastAPI()

#s3fs = open_fs('s3://mybucket/')


# s3 = boto3.client('s3',
#                 endpoint_url='https://s3.us-west-1.wasabisys.com',
#                   aws_access_key_id=config['default']['aws_access_key_id'],
#                   aws_secret_access_key=config['default']['aws_secret_access_key'])

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

@app.get("/buckets")
async def get_buckets() -> Dict [str,List[str]]:
    response = s3.list_buckets()
    bucket_names = [bucket["Name"] for bucket in response["Buckets"]]
    return {"buckets": bucket_names}

@app.get("/objects/{bucket_name}")
async def get_objects(bucket_name: str) -> Dict[str, List[str]]:
    response = s3.list_objects_v2(Bucket=bucket_name)
    object_names = [obj["Key"] for obj in response.get("Contents", [])]
    return {"objects": object_names}


# bucket_name =''
# region = ''
# key_name =''
# file_path =''

# create_bucket(bucket_name, region)
# put_object(file_path, bucket_name, key_name)
# list_objects(bucket_name, 10)
# delete_object(bucket_name, key_name)

fs = s3fs.S3FileSystem(
    key=aws_access_key_id,
    secret=aws_secret_access_key,
    client_kwargs={'endpoint_url': 'https://s3.us-west-1.wasabisys.com'}
)
# file =fs.open(fs.ls('New_Bucket')[0]).read().__dir__()
# print('test')
# os.startfile(file)



# # Retrieve the list of files in the 'New_Bucket' directory
# file_list = fs.ls('New_Bucket')

# # Display the list of files to the user
# print("Files in 'New_Bucket':")
# for i, file_path in enumerate(file_list):
#     print(f"{i+1} - {file_path}")

# # Prompt the user to choose a file
# choice = input("Enter the number of the file you want to open: ")
# choice = int(choice) - 1  # Convert the choice to an integer and adjust for 0-based indexing

# # Validate the user's choice
# if choice < 0 or choice >= len(file_list):
#     print("Invalid choice!")
# else:
#     # Get the chosen file path
#     file_path = file_list[choice]

#     # Extract the file name from file_path
#     file_name = os.path.basename(file_path)

#     # Read the content of the chosen file
#     with fs.open(file_path, 'rb') as file:
#         file_content = file.read()

#     # Create a temporary file with the extracted file name
#     temp_file_path = os.path.join(tempfile.gettempdir(), file_name)
#     with open(temp_file_path, 'wb') as temp_file:
#         temp_file.write(file_content)

#     # Open the temporary file
#     os.startfile(temp_file_path)

#     print("Temporary File Path:", temp_file_path)

file_list = fs.ls('New_Bucket')

# Validate if any files exist in the directory
if not file_list:
    print("No files found in 'New_Bucket' directory.")
else:
    # Get the first file path from the list
    file_path = file_list[0]

    # Extract the file name from file_path
    file_name = os.path.basename(file_path)

    # Read the content of the chosen file
    with fs.open(file_path, 'rb') as file:
        file_content = file.read()

    # Create a temporary file with the same basename as the original file
    temp_file_path = os.path.join(tempfile.gettempdir(), file_name)
    with open(temp_file_path, 'wb') as temp_file:
        temp_file.write(file_content)

    # Open the temporary file
    #os.startfile(temp_file_path)    
    print(temp_file_path)
    file_proc = subprocess.Popen(['start', temp_file_path], shell=False)
    exit_code = file_proc.wait()


    # Read the updated content of the temporary file
    with open(temp_file_path, 'rb') as updated_file:
        updated_content = updated_file.read()

    updated_file_path = os.path.join('New_Bucket', file_name)

    # Save the updated content back to Wasabi
    with fs.open(file_path, 'wb') as updated_file:
        file.write(updated_content)
 
    print("File updated and saved back to Wasabi.")



