from datetime import datetime

from peewee import *

from db import news_db


class User(Model):
    username = CharField(max_length=20, unique=True, null=False, index=True, verbose_name='用户名')
    password = CharField(max_length=16, null=False, verbose_name='用户密码')
    created = DateTimeField(default=datetime.now, formats='YYYY-MM-DD HH:MM:SS')
    updated = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], formats='YYYY-MM-DD HH:MM:SS')

    class Meta:
        database = news_db
        table_name = 'user'

# User.create_table()
