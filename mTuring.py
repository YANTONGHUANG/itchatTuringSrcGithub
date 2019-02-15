# -*- coding: utf-8 -*-
import requests
import json

def turing_communicate_text(w_data):
    if w_data == None or w_data == "":
        return "输入不能为空"
    else:
        data = {
            "reqType": 0,
            "perception": {
                "inputText": {
                    "text": w_data
                },
            },
            "userInfo": {
                "apiKey": "55c69254f0194b1294c68a49a67b8604",
                "userId": "100001"
            }
        }
        ## headers中添加上content-type这个参数，指定为json格式
        headers = {'Content-Type': 'application/json'}
        ## post的时候，将data字典形式的参数用json包转换成json格式。
        response = requests.post(url='http://openapi.tuling123.com/openapi/api/v2', headers=headers, data=json.dumps(data))
        ##解析返回的json文件，提取出其中的回复内容
        reply = json.loads(response.text)['results'][0]['values']['text']
        return reply

if __name__ == "__main__":
    w_data = ""
    print(turing_communicate_text(w_data))