#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import jtalk #OpenJTalk
import talk #talkAPI
import #rulematch

'''認識結果のデータをもらう'''
ID = []  #ID

#sentence.json
with open('sentence.json', 'r') as f:
    sent = json.load(f)#辞書型


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

#resのそれぞれの値が無い時、APIに入力音声テキストを入れる
if res["response"]["txt"]==res["response"]["motion"]==res["response"]["name"]=="":
    res["response"]["txt"] = talk.chat(sent["sentence1"]["sentence"])

    #res.jsonにAPIの出力（テキスト）を書き込む
    with open('res.json','w') as fw:
        json.dump(res, fw, indent=4,ensure_ascii=False)

#音声合成
jtalk.say(res["response"]["txt"])
