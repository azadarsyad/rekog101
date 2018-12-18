import boto3
import requests
import json
import base64

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
		'source': res['SourceImageFace'],
		'match': res['FaceMatches'],
	}
	return result

def lambda_handler(event, context):
	body = json.loads(event['body'])
	img1 = base64.b64decode(body['source'])
	img2 = base64.b64decode(body['target'])
	result = compare_faces(img1, img2)
	return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(result)
    }
