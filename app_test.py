from flask import Flask,request,jsonify
import base64
import re
import socket

import subprocess
import sys
import julius_rec_store as js

"""
それぞれのディレクトリの用途
/image : base64エンコードされた画像をデコードしてローカルに保存する．
/chat : 発話と尤度がペアになったjsonを取得する．
"""

#server
app = Flask(__name__)

@app.route("/")
def index():
    return "send me json "

##発話の認識結果のjsonを保存する
@app.route('/chat', methods=['POST'])
def post_request_chat():
    # Bad request
    if not request.headers['Content-Type'] == 'application/json':
        return jsonify(res='failure'), 400
    ###jsonはdict型なので即変換できないからlistに入れて処理している

    #jsonを取得
    speech = request.json
    print(speech)

    return jsonify(res='success', **speech)

##発話の認識結果のjsonを保存する
@app.route('/scene', methods=['POST'])
def post_request_scene():
    # Bad request
    if not request.headers['Content-Type'] == 'application/json':
        return jsonify(res='failure'), 400
    ###jsonはdict型なので即変換できないからlistに入れて処理している

    #jsonを取得
    input_scene = request.json
    print(input_scene)


    return jsonify(res='success', **input_scene)

if __name__ == "__main__":

    app.debug = True
    app.run("127.0.0.1")
    #app.run("163.225.223.72")
    # curl http://0.0.0.0/post_request -X POST -H "Content-Type: application/json" -}''{"key": "value"}
