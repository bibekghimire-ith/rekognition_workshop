import boto3
import base64

CollectionId="GeneseCollection"

file=open('Sundar.jpg','rb').read()

rekognition_client = boto3.client('rekognition')

response = rekognition_client.index_faces(
    CollectionId=CollectionId,
    Image={
        'Bytes':file
    },
    ExternalImageId="Sundar"
)

print(response)