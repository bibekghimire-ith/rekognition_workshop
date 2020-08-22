import boto3
import os
import base64
import json

# rekognition_client = boto3.client('rekognition',aws_session_token=os.getenv('aws_session_token'),  aws_access_key_id=os.getenv('aws_access_key_id'), aws_secret_access_key=os.getenv('aws_secret_access_key'), region='us-east-1')
rekognition_client = boto3.client('rekognition')
file = open('image1.jpg','rb').read()

response = rekognition_client.detect_faces(
    Image={
        'Bytes':file
    },
    Attributes=['ALL']
)

# print(response['FaceDetails'])

for face in response['FaceDetails']:
    print(json.dumps(face,indent=4,sort_keys=True))