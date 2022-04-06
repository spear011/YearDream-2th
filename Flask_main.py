from flask import Flask, jsonify, render_template
import requests


app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/posts')
def show_posts():
  response = requests.get('https://jsonplaceholder.typicode.com/posts')
  to_serve = response.json()
  return jsonify(to_serve)

if __name__=='__main__':
  app.run(host='0.0.0.0', port=6000, debug=True)

# 프로젝트 시작시 한번만 $ pip install flask
# shell 에서 app 시작 : $ python main.py
