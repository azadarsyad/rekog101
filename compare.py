import boto3
from PIL import Image
import requests

session = boto3.session.Session(profile_name = 'default')
client = session.client('rekognition', 'ap-southeast-2')


def get_image_from_file(filename):
	with open(filename, 'rb') as imgfile:
		return imgfile.read()

def get_image_from_url(url):
	img = Image.open(requests.get(url, stream=True).raw)
	return img

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
	return print(result)


img1 = get_image_from_file('./azad1.jpeg')
img2 = get_image_from_file('./azad2.jpeg')
# img1 = get_image_from_url('https://imgur.com/a/xoeR3xp')
# img2 = get_image_from_url('https://imgur.com/a/yorKwzk')
print(type(img1))

compare_faces(img1, img2)
