import boto3
from PIL import Image
import requests
import json

# session = boto3.session.Session(profile_name = 'default')
client = boto3.client('rekognition', 'ap-southeast-2')

def compare_faces(source, target):
	res = client.compare_faces(
	    SourceImage={
	        'Bytes': source,
	    },
	    TargetImage={
	        'Bytes': target,
	    },
	    SimilarityThreshold=80
	)
	result = {
		'similarity': res['FaceMatches'][0]['Similarity'],
		'confidence': res['FaceMatches'][0]['Face']['Confidence'],
	}
	return result


# img1 = get_image_from_file('./azad1.jpeg')
# img2 = get_image_from_file('./azad2.jpeg')
# img1 = get_image_from_url('https://imgur.com/a/xoeR3xp')
# img2 = get_image_from_url('https://imgur.com/a/yorKwzk')
# print(img1)

def lambda_handler(event, context):
	img1 = event['source']
	img2 = event['target']
	result = compare_faces(img1, img2)
	return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
