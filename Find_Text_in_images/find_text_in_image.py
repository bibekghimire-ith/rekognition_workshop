import boto3
import base64

rekognition_client = boto3.client('rekognition')

file = open('image2.png','rb').read()

response = rekognition_client.detect_text(
    Image={
        'Bytes':file
    }
)

texts = []

for text in response['TextDetections']:
    if(text['Type'] == "WORD"):
        texts.append(text['DetectedText'])
print(" ".join(texts))
