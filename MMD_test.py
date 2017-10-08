#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import jtalk #OpenJTalk
import talk #talkAPI
from rule_base import res7
import julius
import app_test as app
import socket

host = "127.0.0.1" #お使いのサーバーのホスト名を入れます
port = 5000 #クライアントと同じPORTをしてあげます

serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversock.bind((host,port)) #IPとPORTを指定してバインドします



while True: #認識開始のループ
	serversock.listen(10)
	clientsock, client_address = serversock.accept() #接続されればデータを格納
	print("flag")

	'''認識結果のデータを読み込む'''
	#IDは画像から物体認識や動作認識が終わったあと

	#speech: speech.jsonの情報
	#input_scene: scene.jsonの情報
	'''
	with open("data2/koresuki.json") as f:
		speech = json.load(f)
	'''


	with open("data2/data2.json") as fw:
		scene = json.load(fw)

	while True:
		rcvmsg = clientsock.recv(4096) #ここの時点でbytes

		rcvmsg = rcvmsg.decode('utf-8')
        #rcvmsg = rcvmsg.encode('utf-8')
		rcvmsg = json.loads(rcvmsg)
		print('Received -> ')
		print(rcvmsg)
		#clientsock.close()

		#仮に
		speech = rcvmsg

		#res.jsonの辞書型オブジェクト res を受け取る
		#res.jsonのファイル保存はルールマッチプログラム内ではやらない
		res = res7.main(speech, scene)

		#resのそれぞれの値が無い時、APIに入力音声テキストを入れる
		'''
		if res["response"]["txt"]==res["response"]["motion"]==res["response"]["name"]=="":
			res["response"]["txt"] = talk.chat(speech["sentence1"]["sentence"])
		'''
		if res["RESPONSE"]==res["ID"]==res["ORDER"]=="":
			res["RESPONSE"] = talk.chat(res["input_txt"])

		if res["RESPONSE"] == "":
			#0.1秒待ってから入力開始へ
			print("0.1秒待つ")
			break
		else:
			#書き込み
			print(res)
			with open('res.json','w') as fw:
				json.dump(res, fw, indent=4,ensure_ascii=False)
			#ロボット動作と音声合成へ
			##今は仮に
			break
			'''
			音声合成
    		jtalk.say(res["response"]["txt"])
			'''
