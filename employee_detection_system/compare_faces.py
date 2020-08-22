import boto3
import base64
import json

CollectionId="GeneseCollection"

file=open('dangal.jpg','rb').read()

rekognition_client = boto3.client('rekognition')

response = rekognition_client.search_faces_by_image(
    CollectionId=CollectionId,
    Image={
        'Bytes':file
    }
)

print(json.dumps(response['FaceMatches'],indent=4,sort_keys=True))