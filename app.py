from flask import Flask
import os
import dotenv 
import requests

dotenv.load_dotenv('./.env')

access_key = os.environ.get('ACCESS_KEY') 
secret_key = os.environ.get('SECRET_KEY')

auth_header = {'X-ApiKeys': f'accessKey={access_key}; secretKey={secret_key}'}

app = Flask(__name__)

def get_images(offset=0, limit=50):
    url = 'https://cloud.tenable.com/container-security/api/v2/images' 
    querystring = {'offset': offset, 'limit': limit} 
    headers = {**{'Accept': 'application/json'}, **auth_header}
    response = requests.request('GET', url, headers=headers, params=querystring)
    return response.json()


@app.route('/images')
def list_images():
    return get_images()
