#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import jtalk #OpenJTalk
import talk #talkAPI
import #rulematch

#socket 通信準備

while True: 
	#認識開始トリガ
	
	#speech, scene を初期化
    #socket 通信
    while True: #認識開始
	    #socket 通信のrecv 
	    #resのそれぞれの値が無い時、APIに入力音声テキストを入れる
	    if res["response"]["txt"]==res["response"]["motion"]==res["response"]["name"]=="":
    		res["response"]["txt"] = talk.chat(speech["sentence1"]["sentence"])

    		#res.jsonにAPIの出力（テキスト）を書き込む
    		with open('res.json','w') as fw:
        		json.dump(res, fw, indent=4,ensure_ascii=False)


 	     #ロボット動作
	     #音声合成
	     jtalk.say(res["response"]["txt"])
	     break
