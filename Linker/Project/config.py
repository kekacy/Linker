import os
import sys
from Linker import app

SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')

# # SQLite URI compatible
# WIN = sys.platform.startswith('win')
# if WIN:
#     prefix = 'sqlite:///'
# else:
#     prefix = 'sqlite:////'
# dev_db = prefix + os.path.join(os.path.dirname(app.root_path), 'data.db')
# #要不要动态跟踪修改（不建议修改，未来版本会移除）
# SQLALCHEMY_TRACK_MODIFICATIONS = False
# SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)
# python3不支持mysqldb，因此使用pymysql替代
DIALCT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'Hhf1234./'
HOST = '8.140.116.23'
PORT = '3306'
DBNAME = 'db_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALCT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DBNAME)
