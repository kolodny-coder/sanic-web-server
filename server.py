from sanic.response import json

from auth import protected
from login import login
from sanic import Sanic

app = Sanic("AuthApp")
app.config.SECRET = "KEEP_IT_SECRET_KEEP_IT_SAFE"
app.blueprint(login)


@app.post("/secret")
@protected
async def test(request):
    return_dict = {}
    for i in request.json:
        return_dict.update({i['name']: [v for k, v in i.items() if "Val" in k][0]})
    return json(return_dict, status=201)


if __name__ == '__main__':
    app.run(debug=True)
