#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import jtalk #OpenJTalk
import talk #talkAPI
import #rulematch


while True:

	'''認識結果のデータを読み込む'''
	#IDは画像から物体認識や動作認識が終わったあと
	#指差し情報（座標情報込み？）windowsからubuntuに送られてくる

	#speech: speech.jsonの情報
	#input_scene: scene.jsonの情報
	while True:
	    '''
    	ルールベース対話にマッチするかどうか
        IDとsent を入力
        出力はJSON形式「res.json」(ルールマッチ関数内で保存しておく)
        {
   			"response":{
     		"txt" : "",
     		"motion" : "",
     		"ID" : ""
   			}
		}
		この関数の出力は辞書型オブジェクト
		'''
		#res.jsonの辞書型オブジェクト res を受け取る
		res = {
   			"response":{
     		"txt" : "",
     		"motion" : "",
     		"ID" : "",
			"in_txt" : "" #in_txtはルールマッチしないときのみ？
   			}
		}

		#resのそれぞれの値が無い時、APIに入力音声テキストを入れる
		if res["response"]["txt"]==res["response"]["motion"]==res["response"]["name"]=="":
    		res["response"]["txt"] = talk.chat(speech["sentence1"]["sentence"])

		if res["response"]["txt"] == "":
			break
		else:
			#書き込み
			#




    		#res.jsonにAPIの出力（テキスト）を書き込む
			#res.jsonの保存はこっちでする（ルールマッチのほうではやらない）
    		with open('res.json','w') as fw:
        		json.dump(res, fw, indent=4,ensure_ascii=False)


 		#ロボット動作
		#音声合成
		jtalk.say(res["response"]["txt"])
		break
