from flask import Flask, render_template, request
import stream_chat
from datetime import datetime
import os
from dotenv_config import Config


# current date and time
now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

config = Config('.env')
STREAM_API_SECRET = Config('STREAM_API_SECRET')  # str

app = Flask(__name__)
@app.route('/firebase', methods=["GET", "POST"])
def home():

    # example: http://127.0.0.1:5000/firebase?uid=325245&name=idan
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
        'get_api_call_at' : f'{now}',
        'firebase_uid' : f'{uid}',
        'firebase_name' : f'{name}',
        'getStream_token' : f'{token}'
    }

if __name__ == '__main__':
    app.run(debug=True)
