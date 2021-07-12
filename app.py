# 공공데이터활용지원센터_코로나19 예방접종 통계 데이터 조회 서비스

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
app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.covid

key = "4MZE91nl58LxJryx5TYngBgW4jTxjLlYQlteJ3kTud9MYYFJKO8khFD%2BeeJRqD%2FQGeT8jlwOJVBASEUXoiborw%3D%3D"
requesturl = "http://api.odcloud.kr/api/15077756/v1/vaccine-stat?page=1&perPage=10&serviceKey=4MZE91nl58LxJryx5TYngBgW4jTxjLlYQlteJ3kTud9MYYFJKO8khFD%2BeeJRqD%2FQGeT8jlwOJVBASEUXoiborw%3D%3D"

## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# (POST) API
@app.route('/covid', methods=['POST'])
def save_order():
    # sample_receive = request.form['sample_give']
    # print(sample_receive)
    return jsonify({'msg': '이 요청은 POST!'})


# 목록보기(Read) API
@app.route('/covid', methods=['GET'])
def view_vaccine():
    sample_receive = request.args.get(requesturl+key)
    return jsonify(sample_receive)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)