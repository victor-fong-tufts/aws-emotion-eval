import boto3
from PIL import Image
import io
local='images/deploy.jpg'
client = boto3.client('rekognition', region_name='us-east-1')
image = Image.open(local)

stream = io.BytesIO()
image.save(stream,format="JPEG")
image_binary = stream.getvalue()

response = client.detect_labels(
    Image={'Bytes':image_binary}
    )


print(response) 
