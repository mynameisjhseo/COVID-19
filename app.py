from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
from urllib.parse import urlencode, unquote
import requests
import json

app = Flask(__name__)
# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.dpsparta

## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')

# (POST) API
@app.route('/center', methods=['GET'])
def get_center():
    centers = list(db.center.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'centers': centers})

# find API
@app.route('/find', methods=['GET'])
def find_vaccine():
    url = 'https://api.odcloud.kr/api/15077586/v1/centers?page=1&perPage=1000&serviceKey=4MZE91nl58LxJryx5TYngBgW4jTxjLlYQlteJ3kTud9MYYFJKO8khFD%2BeeJRqD%2FQGeT8jlwOJVBASEUXoiborw%3D%3D'
    response = requests.get(url)
    r_dict = json.loads(response.text)
    r_response = r_dict.get("data")
    id = r_response[0].get("id")
    data = list(db.center.find({'id': id}))
    print(data)
    return jsonify({'what': 'what'})

# OPEN API
@app.route('/covid', methods=['GET'])
def view_vaccine():
    url = 'https://api.odcloud.kr/api/15077586/v1/centers?page=1&perPage=1000&serviceKey=4MZE91nl58LxJryx5TYngBgW4jTxjLlYQlteJ3kTud9MYYFJKO8khFD%2BeeJRqD%2FQGeT8jlwOJVBASEUXoiborw%3D%3D'
    response =\
        requests.get(url)
    r_dict = json.loads(response.text)
    r_response = r_dict.get("data")
    for res in r_response:
        id = res.get("id")
        data = list(db.center.find({'id': id}))
        if (len(data) == 0):
            center = {
                'address' : res.get("address"),
                'centerName' : res.get("centerName"),
                'centerType' : res.get("centerType"),
                'createdAt' :  res.get("createdAt"),
                'facilityName' : res.get("facilityName"),
                'id' : res.get("id"),
                'lat' : res.get("lat"),
                'lng' : res.get("lng"),
                'org' :res.get("org"),
                'phoneNumber' : res.get("phoneNumber"),
                'sido' : res.get("sido"),
                'sigungu' : res.get("sigungu"),
                'updatedAt' : res.get("updatedAt"),
                'zipCode' : res.get("zipCode")
            }
            db.center.insert_one(center)

    return jsonify({'what':'what'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
