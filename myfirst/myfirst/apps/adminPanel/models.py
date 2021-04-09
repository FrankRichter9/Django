from django.db import models

class Article(models.Model):
    article_title = models.CharField('article name', max_length = 200)
    article_text = models.TextField('article text')



class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    author_name = models.CharField('name author', max_length = 50)
    comment_text = models.CharField('comment text', max_length = 200)
