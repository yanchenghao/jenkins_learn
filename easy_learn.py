import os
import requests
def hello():
    print("hello world")

import os
# from robot_learn import login
URL="https://oapi.dingtalk.com/robot/send?access_token=5b6e13315bf24a0a6cc18d299354d1745a41df6da6ce295763e0e55f7e223885"
def dd_notify():
  body={
    "text": {
        "content": "关键字"+": "+"mac 发送1"
    },
    "msgtype": "text"
   }
  res = requests.post(URL, json=body, timeout=2)
# os.system("/Users/yanchenghao/PycharmProjects/venv5/bin/python /Users/yanchenghao/PycharmProjects/PycharmProjects/pythonProject/robot_learn/hello.py")
dd_notify()