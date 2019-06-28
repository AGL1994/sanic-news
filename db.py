import peewee_async
db = {
    'user': 'root',
    'host': '192.168.88.157',
    'password': '123456',
    'port': 3306,
    'max_connections': 10
}
news_db = peewee_async.PooledMySQLDatabase('wordpress', **db)
objects = peewee_async.Manager(news_db)
# 数据库常量

# NEWS_TECHNOLOGY, NEWS_STAR, NEWS_SPORTS, NEWS_
# NEWS_TYPE = (
#     (, ''),
#     (, ''),
#     (, ''),
#     (, ''),
# )
