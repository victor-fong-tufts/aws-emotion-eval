import boto3
from PIL import Image
import io
local='images/surprised_woman_02.jpg'
client = boto3.client('rekognition', region_name='us-east-1')
image = Image.open(local)

stream = io.BytesIO()
image.save(stream,format="JPEG")
image_binary = stream.getvalue()

response = client.detect_faces(
    Image={'Bytes':image_binary}, Attributes=['ALL']
    )


print(response) 
