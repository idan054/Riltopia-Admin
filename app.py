from flask import Flask, render_template, request
import stream_chat
from datetime import datetime
from dotenv_config import Config

### HOW TO CREATE NEW HEROKU PROJECT! ###
#1 Fork this repo: https://github.com/idan054/Riltopia-Admin/tree/ad39fd314792d7192d7c78d31030b046f31f3161
#2 Create heroku app > Deploy tab > connect github > click deploy.
# * U might need to run $ heroku login && heroku restart

# current date and time
now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

config = Config('.env')
STREAM_API_SECRET = Config('STREAM_API_SECRET')  # str

app = Flask(__name__)
@app.route('/', methods=["GET", "POST"])
def home():
    return {
        'status': 200,
        'details' : 'Use /firebase?name=NAME&uid=UID, only UID is required',
        'example' : 'https://riltopia-admin.herokuapp.com/firebase?uid=325245&name=idan'
    }

@app.route('/firebase', methods=["GET", "POST"])
def firebase():
    # example: http://127.0.0.1:5000/firebase?uid=325245&name=idan
    # heroku: https://riltopia-admin.herokuapp.com/firebase?uid=325245&name=idan
    print('Start:')
    args = request.args
    uid = args.get('uid')
    name = args.get('name')
    print(f'{uid} - {name}')

    server_client = stream_chat\
        .StreamChat(api_key="ah48ckptkjvm",
                    api_secret=f"{STREAM_API_SECRET}")

    token = server_client.create_token(f'{uid}')
    print(f'token {token}')

    # return render_template("base.html")
    return {
        'status' : 201,
        'details' : 'get stream token success',
        'deleteMe_key': 'ah48ckptkjvm',
        'deleteMe_Secret': f'{STREAM_API_SECRET}',
        'get_api_call_at' : f'{now}',
        'firebase_uid' : f'{uid}',
        'firebase_name' : f'{name}',
        'getStream_token' : f'{token}'
    }

if __name__ == '__main__':
    app.run(debug=True)
