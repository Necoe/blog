from models.article import Article
from routes import db

class  ArticleService:
    def get_article(self,id):
        return db.session.get(Article, id)
