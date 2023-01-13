""" 
Path    : config.py.py
Function:
coding  : utf-8
Version : V1.0
Time    : 2023/1/11 22:11
Author  : Walon Cyler
Modified: 
"""


DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = '303544'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'accounting'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME,
                                                                       PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False