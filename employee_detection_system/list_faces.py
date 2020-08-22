import boto3
import json

CollectionId="GeneseCollection"


rekognition_client = boto3.client('rekognition')

response = rekognition_client.list_faces(
    CollectionId=CollectionId,
)

for face in response['Faces']:
    print(json.dumps(face,indent=4,sort_keys=True))