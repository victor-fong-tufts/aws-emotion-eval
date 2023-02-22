import boto3
from PIL import Image
import io
import json
local='images/woman_sofa_side.jpg'
client = boto3.client('rekognition', region_name='us-east-1')
image = Image.open(local)

stream = io.BytesIO()
image.save(stream,format="JPEG")
image_binary = stream.getvalue()

response = client.detect_faces(
    Image={'Bytes':image_binary}, Attributes=['ALL']
    )


print(json.dumps(response))
