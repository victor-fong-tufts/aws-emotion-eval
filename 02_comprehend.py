import boto3
from PIL import Image
import io
import json

with open('text/03_neutral.txt') as f:
    lines = f.readlines()

line = ' '.join(lines)

client = boto3.client('comprehend', region_name='us-east-1')

response = client.detect_sentiment(
    Text=line, LanguageCode='en'
)


print(json.dumps(response))
