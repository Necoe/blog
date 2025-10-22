from flask import Flask

from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__,
            template_folder='../templates',
            static_folder='../assets',
            static_url_path='/assets')

user = 'postgres'  # 默认的超级管理员用户
password = '621700'
host = 'localhost'
port = '5432'
database = 'myblog_db'


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:621700@localhost:5432/myblog_db'

db= SQLAlchemy(app)



from routes import user_routes
from routes import admin_routes