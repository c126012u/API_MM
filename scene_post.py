# -*- coding:utf-8 -*-
import socket
import json

host = "127.0.0.1" #お使いのサーバーのホスト名を入れます
port = 5000 #適当なPORTを指定してあげます

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #オブジェクトの作成をします

client.connect((host, port)) #これでサーバーに接続します

obj = {
        "20":{
            "locaton":["x", "y", "z"],
            "motion":"POINTING",
            "name":[
                "ねこ",
                "いぬ",
                "エルモ",
                "ピカチュウ",
                "トトロ"
            ],
            "confidence":[
                "50.0",
                "16.0",
                "14.0",
                "11.0",
                "9.0"
            ]
        },
        "11":{
            "locaton":["x", "y", "z"],
            "motion":"",
            "name":[
                "いぬ",
                "エルモ",
                "トトロ",
                "ねこ",
                "ピカチュウ"
            ],
            "confidence":[
                "60.0",
                "20.0",
                "17.0",
                "15.0",
                "10.0"
            ]
        }

    }

obj_sock = json.dumps(obj)


client.send(obj_sock.encode('utf-8')) #適当なデータを送信します（届く側にわかるように）

client.close()
