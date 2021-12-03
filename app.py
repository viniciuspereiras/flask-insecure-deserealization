from logging import debug
from flask import Flask, request
import pickle
import base64

app = Flask(__name__)

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def name(self):
        return self.name

admin = User('admin', 'admin@cius.xyz', 'admin')
cookie = pickle.dumps(admin)
print(base64.b64encode(cookie).decode('utf-8'))

@app.route('/')
def index():
    if request.cookies.get('session'):
        cookies = request.cookies.get('session')
        cookies = base64.b64decode(cookies)
        cookies = pickle.loads(cookies)
        return f'<h1>Hello {cookies.name}!</h1>'
    else:
        return '<h1>Hello World!</h1>'

app.run(host='0.0.0.0', port=8080, debug=True)