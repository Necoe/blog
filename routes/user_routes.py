from routes import app
from flask import abort, render_template
from services.article_service import ArticleService

@app.route('/')
@app.route('/index.html')
def index():

    return render_template('index.html')


@app.route('/article/<article_id>.html')  # <article_id> 可变量，从浏览器输入的值可以传入下面的函数中参数,再用服务函数调用来确定数据库中数据
def article_page(article_id):
    article = ArticleService().get_article(article_id)

    if article:
        return render_template('article.html',article = article)
    
    abort(404)



@app.route('/about.html')
def about():
    return render_template('about.html')





@app.route('/login.html')
def login():
    return "Loign page"
