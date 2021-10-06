import jwt
from sanic import Blueprint, text
from users_secrets import users_dict
from sanic.response import json
import json

login = Blueprint("login", url_prefix="/login")


@login.post("/")
async def do_login(request):
    print(request.json)
    user = request.json["username"]
    password = request.json["pass"]
    if users_dict.get(user) != password:
        return json({"message": "The user not listed in Db or Wrong Password"})

    token = jwt.encode({}, request.app.config.SECRET)
    return text(token)
