from boto3 import client
from boto3 import resource
from botocore.exceptions import ClientError
import zipfile 
import os

def makeZip():
    zf = zipfile.ZipFile("Jenkins.zip", "w")
    for dirname, subdirs, files in os.walk('/jenkins'):
        zf.write(dirname)
        for filename in files:
            zf.write(os.path.join(dirname, filename))
    zf.close()

def uploadFiles2Bucket(file_name, bucket_name):
        s3client = client('s3')
        object_name  = file_name
        try:
            with open(file_name, "rb") as f:
                s3client.upload_fileobj(f, bucket_name, object_name, ExtraArgs={
        "ContentType": 'zip', 'ACL': "public-read"
        } )
        except ClientError as e:
            logging.error(e)
            return None
        return object_name


makeZip()
#if uploadFiles2Bucket('Jenkins.zip', 'jenkins-cicd-1002'):
print("SUCCESS")
