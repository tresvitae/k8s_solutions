from flask import Flask
from flask import request
import os

app = Flask(__name__)


@app.route('/pods/env-var')
def get_env_variable():
    env_name = request.args.get('variable')
    if env_name in os.environ:
        return f"Hello {os.environ[env_name]}!"
    else:
        return "Hello anonymous!"
    
@app.route('/pods/env-vars')
def get_env_variables():
    return dict(os.environ)

@app.route('/')
def index():
    return "Hello in Kubernetes course!"


if __name__ == '__main__':
    app.run(host='0.0.0.0')