from flask import Flask
import argparse
from flask import request

app = Flask(__name__)


def read_valid_users():
    return {
        "paul": "paul",
        "nora": "nora",
        "david": "david",
        "kumar": "kumar",
    }


def valid_login(username, password):
    valid_users = read_valid_users()
    if username in valid_users and valid_users[username] == password:
        return True
    return False


@app.route('/')
def hello_world():
    return '<h1>Yay,you got it working</h1>'


@app.route('/login', methods=["POST"])
def auth():
    ret=None
    if request.method == 'POST':
        if valid_login(request.form.get('username',None),
                       request.form.get('password',None)):
            ret= "Ok",200
        else:
            ret = 'Invalid username/password',401
        # the code below is executed if the request method
        # was GET or the credentials were invalid
    return ret


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Runs mock HTTP server')
    parser.add_argument('--port', default=5009,
                        help='Runs the server on a given port.')

    args = parser.parse_args()
    app.run(host="0.0.0.0",port=args.port, debug=True)
