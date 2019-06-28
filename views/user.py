from sanic import Blueprint
from sanic.response import json

from db import objects
from models.user import User

bp = Blueprint('bp')


@bp.route('/user', methods=['POST'])
async def create_user_view(request):
    await objects.create(User, username='admin', password='123456')
    return json({"hello": "world"})


@bp.route('/user/1', methods=['PUT'])
async def create_user_view(request):
    # user = await objects.get(User, id=1)
    # user = User()
    await objects.execute(
        User.update(
            username='张三'
        ).where(
            id == 1
        )
    )
    # await objects.update(user)
    return json({"hello": "world"})
