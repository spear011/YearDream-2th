from flask import Flask, jsonify, render_template
import requests


app = Flask(__name__)

@app.route('/') #decorator
def index():
  return render_template('index.html')

# index.html
#<!doctype html>
# <html>
#   <h1>Home</h1>
#   <p>This is home.</p>
# </html>
  
# routing: 사용자의 접속 경로를 지정
# rendering : 페이지를 그려내는것
# 외부 api 정보 가져오기

@app.route('/posts')
def show_posts():
  response = requests.get('https://jsonplaceholder.typicode.com/posts')
  to_serve = response.json()
  return jsonify(to_serve)

# /todos -> "This is todos"

if __name__=='__main__':
  app.run(host='0.0.0.0', port=4000, debug=True)
  # 프로젝트 첫 시작시(한번만) $ pip install flask
  # shell에서 app 시작: $ python main.py
