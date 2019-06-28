from datetime import datetime

from peewee import *


# 新闻
from db import news_db
from models.user import User


# 新闻分类
class NewsType(Model):
    title = CharField(max_length=20, verbose_name='分类', unique=True, null=False)
    created = DateTimeField(default=datetime.now, formats='YYYY-MM-DD HH:MM:SS')

    class Meta:
        database = news_db


# 新闻
class News(Model):
    author = ForeignKeyField(User, backref='author', lazy_load=False, verbose_name='作者')
    type = ForeignKeyField(NewsType, backref='type', lazy_load=False, verbose_name='分类')
    title = CharField(unique=True, max_length=100, null=False, index=True, verbose_name='标题')
    created = DateTimeField(default=datetime.now, formats='YYYY-MM-DD HH:MM:SS')
    updated = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], formats='YYYY-MM-DD HH:MM:SS')

    class Meta:
        database = news_db
