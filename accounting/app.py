from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

from models import *

#  新增数据
@app.route('/addData')
def addData():
    article = Article(title='蒙牛与伊利开箱评测', content='这篇文章写的很好！')
    db.session.add(article)
    db.session.commit()
    return 'Hello World!'

@app.route('/')
def hello_world():
    return 'shit!'

if __name__ == '__main__':
    app.run()