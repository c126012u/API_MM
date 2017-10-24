# -*- coding:utf-8 -*-
import socket
import json
import sys
import urllib.request


#print("data1:API用")
#print("data2:エルモとピカチュウとねこ")
#print("data3:りんごとバナナ")

#data = sys.stdin.readline()
data = "data1\n"
url = "http://0.0.0.0:5000/scene_test"
method = "POST"
headers = {"Content-Type" : "application/json"}

if data == "data1\n":
    with open("data1/data1.json") as f:
        obj = json.load(f)
elif data == "data2\n":
    with open("data2/data2.json") as f:
        obj = json.load(f)
elif data == "data3\n":
    with open("data3/data3.json") as f:
        obj = json.load(f)
json_data = json.dumps(obj).encode("utf-8")
# httpリクエストを準備してPOST
request = urllib.request.Request(url, data=json_data, method=method, headers=headers)
with urllib.request.urlopen(request) as response:
    response_body = response.read().decode("utf-8")
