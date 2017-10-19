#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import jtalk #OpenJTalk
import talk #talkAPI
from rule_base import res7
import socket
import time
import sys

host = "127.0.0.1"

#sceneサーバ側
sc_port = 5001
sc_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sc_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sc_sock.bind((host,sc_port)) #IPとPORTを指定してバインドします

#speechサーバ側
sp_port = 5000
sp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sp_sock.bind((host,sp_port)) #IPとPORTを指定してバインドします

while True:

	print("認識開始:Enter")
	trig = sys.stdin.readline()
	speech = {'sentence1': {'sentence': '', 'score': '0', 'word': [], 'CM': []}, 'sentence2': {'sentence': '', 'score': '0', 'word': [], 'CM': []}, 'sentence3': {'sentence': '', 'score': '0', 'word': [], 'CM': []}, 'sentence4': {'sentence': '', 'score': '0', 'word': [], 'CM': []}, 'sentence5': {'sentence': '', 'score': '0', 'word': [], 'CM': []}, 'sentence6': {'sentence': '', 'score': '0', 'word': [], 'CM': []}, 'sentence7': {'sentence': '', 'score': '0', 'word': [], 'CM': []}, 'sentence8': {'sentence': '', 'score': '0', 'word': [], 'CM': []}, 'sentence9': {'sentence': '', 'score': '0', 'word': [], 'CM': []}, 'sentence10': {'sentence': '', 'score': '0', 'word': [], 'CM': []}}
	scene = {'':{'location':[],'motion':'','name':[],'confidence':[]} }
	res = {}

	sc_sock.listen(1)
	sc_sock.setblocking(False)
	sp_sock.listen(1)
	sp_sock.setblocking(False)
	#認識開始のループ
	while trig == "\n":
		#print("接続準備")
		try:
			sc_client, sc_address = sc_sock.accept()
			scene = sc_client.recv(4096) #ここの時点でbytes
			scene = scene.decode('utf-8')
			scene = json.loads(scene)
			print('Received -> ')
			print(scene)

		except BlockingIOError:
			time.sleep(0.1)
			print("sceneなし")

		try:
			sp_client, sp_address = sp_sock.accept()
			speech = sp_client.recv(4096) #ここの時点でbytes
			speech = speech.decode('utf-8')
			speech = json.loads(speech)
			print('Received -> ')
			print(speech)

		except BlockingIOError:
			time.sleep(0.1)
			print("speechなし")
		try:
			res = res7.main(speech, scene)
		except UnboundLocalError:
			time.sleep(0.1)
			pass
		except TypeError:
			time.sleep(0.1)
			pass

		if res == {}: #音声なし、ルールマッチなし
			print("0.1秒待つ")
			time.sleep(0.1)
			pass
		#音声なし、ルールマッチあり
		elif res["ID"]!="" and res["RESPONSE"]=="" and res["ORDER"]!="":
			print("ロボット")
			trig = "" ##認識開始前にもどる
			break
		elif res["RESPONSE"]==res["ID"]==res["ORDER"]=="":#音声有り、ルールマッチなし
			res["RESPONSE"] = talk.chat(res["input_txt"])
			print(res)
			jtalk.say(res["RESPONSE"])
			trig = "" ##認識開始前にもどる
			break

		else:
			#書き込み
			print(res)
			with open('res.json','w') as fw:
				json.dump(res, fw, indent=4,ensure_ascii=False)
			jtalk.say(res["RESPONSE"])
			trig = "" ##認識開始前にもどる
			break

	sc_client.close()
	sp_client.close()
