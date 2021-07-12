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

# 달력
# https://colorlib.com/wp/bootstrap-calendars/

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
