# -- coding: utf-8 --
import requests
from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/',methods=['POST'])
def alarms():
   data = json.loads(request.data)
   data = json.dumps(data, indent=2)
   headers = {
       "Authorization": "Bearer " + 'LqzzHSaoyUQcD71fLETnqNOp8D8hWvdQxIQ8IWLH8YL', # 貼上Token
       "Content-Type": "application/x-www-form-urlencoded"
    }
   payload = {'message': data}
   r = requests.post("https://notify-api.line.me/api/notify", headers=headers, params=payload)
   # return r.status_code
   return 'OK'


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5001, debug=False)

