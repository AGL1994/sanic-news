from sanic import Sanic

from views.user import bp as user_bp

app = Sanic()
app.blueprint(user_bp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
