from app import app

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/ping')
def ping_pong():
    return 'pong'