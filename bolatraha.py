import json
from random import randint
from flask import Flask, render_template, request
from tinydb import TinyDB
from time import strftime


app = Flask(__name__)
db = TinyDB('blog.json')
app.config['SECRET_KEY'] = str(randint)

@app.route('/', methods=['GET'])
def hello_world():
    posts = db.all()
    return render_template('index.html', thoughts=posts)


@app.route('/record', methods=['GET'])
def record_get():
    return render_template('record.html')


@app.route('/record', methods=['POST'])
def record_post():
    data = request.form
    title = data['title']
    thoughts = data['thoughts']
    name = data['author']
    cat = data['cat']
    db.insert(
        {'thoughts': thoughts,
         'name': name,
         'title': title,
         'cat': cat,
         'time': strftime("%Y-%m-%d %H:%M:%S")})

    return render_template('confirm.html')



if __name__ == '__main__':
    app.run()
