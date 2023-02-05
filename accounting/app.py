from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger, swag_from

import apis as swag_file
from models import *


app = Flask(__name__)
Swagger(app)
# app.config.from_pyfile('config.py')
app.config['JSON_AS_ASCII'] = False
db = SQLAlchemy(app)


@app.route('/addData')
def addData():
    article = Article(title='蒙牛与伊利开箱评测', content='这篇文章写的很好！')
    db.session.add(article)
    db.session.commit()
    return 'Hello World!'


@app.route('/v0/accounting', methods=['GET'])
@swag_from(swag_file.accounting_get)
def demo_get_request():
    """
    ---
    tags:
      - Accounting API
    """
    return "pass!"


@app.route('/v0/accounting', methods=['POST'])
@swag_from(swag_file.accounting_post)
def demo_request():
    """
    ---
    tags:
      - Accounting API
    """
    json_data = request.json
    result = {"code":"200", "msg":"SUCCESS","data":{"name":"xyan","age":25,"job":"python"}}
    return jsonify(result)

if __name__ == '__main__':
    app.run(port=5200, debug=True)