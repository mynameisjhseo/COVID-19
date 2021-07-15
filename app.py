# 공공데이터활용지원센터_코로나19 예방접종 통계 데이터 조회 서비스
# front-end
# https://onepagelove.com/huddle
# https://onepagelove.com/github-contributions
# https://www.pinterest.co.kr/pin/376543218851337038/
# https://velog.io/@eunjin/Javascript-Toy-Project-Random-Meal-Generator-%EC%98%A4%EB%8A%98%EB%AD%90%EB%A8%B9%EC%A7%80-%ED%86%A0%EC%9D%B4%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8
# https://www.pinterest.co.kr/pin/389068855304019276/
# https://www.pinterest.co.kr/pin/745416175808909677/
# https://www.pinterest.co.kr/pin/375417318941596349/
# https://www.pinterest.co.kr/pin/150237337558067764/

# https://www.pinterest.co.kr/pin/9499849194764961/
# https://colorlib.com/wp/free-inquiry-form-templates/

# 예시1
# https://velog.io/@gurumagineer/1%EC%B0%A8-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%ED%9B%84%EA%B8%B0


# 예시 3
# https://corona-live.com/vaccine/

# 템플릿 1
# https://dashboardpack.com/live-demo-preview/?livedemo=378797

# 템플릿 2
# https://dashboardpack.com/live-demo-preview/?livedemo=1881?utm_source=colorlib&utm_medium=reactlist&utm_campaign=architectangular

# 달력
# https://colorlib.com/wp/bootstrap-calendars/

# 기능 참고
# https://korean.cdc.gov/coronavirus/2019-ncov/index.html

# 지도
# https://seunghyum.github.io/about/#
# https://navermaps.github.io/maps.js.ncp/docs/tutorial-2-Getting-Started.html
# EndPoint
# https://infuser.odcloud.kr/oas/docs?namespace=15077756/v1

# Encoding Key
# 4MZE91nl58LxJryx5TYngBgW4jTxjLlYQlteJ3kTud9MYYFJKO8khFD%2BeeJRqD%2FQGeT8jlwOJVBASEUXoiborw%3D%3D

# Decoding Key
# 4MZE91nl58LxJryx5TYngBgW4jTxjLlYQlteJ3kTud9MYYFJKO8khFD+eeJRqD/QGeT8jlwOJVBASEUXoiborw==

# Get
# /15077756/v1/vaccine-stat

from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
from urllib.parse import urlencode, unquote
import requests
import json

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.dpsparta

## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('test.html')


## HTML 화면 보여주기
@app.route('/icons')
def icons():
    return render_template('./examples/icons.html')

## HTML 화면 보여주기
@app.route('/backup')

def backup():
    return render_template('backup.html')

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
    response = requests.get(url)
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
