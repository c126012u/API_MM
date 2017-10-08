# -*- coding: utf-8 -*-
#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function
import socket
from contextlib import closing
import subprocess
import re
import sys
import julius_rec_store as js
import urllib.request, json
import base64
import collections as cl

'''
speech.jsonを保存できたらサーバへ送信
'''

def main():


    host = "localhost"
    port = 10500
    bufsize = 4096
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host,port))

    #待機コマンド
    ##sock.send(b'PAUSE\n')

    #再開コマンド
    ##sock.send(b'RESUME\n')
    while True: #recv_data を受け取ってない時のループ、このループがないと１回の結果受け取りでプログラムが終了する
        sentence_data = [] #１０個の文字列格納
        score_data = [] #１０個の尤度格納
        matchs = [] #１つの文字列取り出し
        CM= [] #1つの単語信頼度取り出し
        CM_list = [] #単語信頼度リスト
        word_list = [] #単語ごとに文字列をリストに入れる

        while True:

            '''juliusの音声認識受け取り'''
            recv_data = sock.recv(bufsize)

            #recv_data = recv_data.encode("utf-8")
            recv_data = recv_data.decode("utf-8")
            ##クライアント側：UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe3 in position 4095: unexpected end of data
            ##サーバ側:とくにエラー無し
            ##このエラーがたまに出る（プログラムが終了してしまう）

            #Error: module_send:: Connection reset by peer

            with open('julius_N.log', mode='w') as a_file:
                a_file.write(recv_data)#juliusの認識結果全部をファイルに書き込み

            '''一行ごとに読み込み'''
            with open('julius_N.log', 'r') as f:
                recv_line = f.readlines()

            '''認識結果の取り出し（1行毎）'''
            for i in range(len(recv_line)):
                '''文字列（1文）取り出し'''
                pattern = r'WORD="(.*?)"'
                match = re.findall(pattern, recv_line[i])
                matchs = matchs + match
                moji = "".join(matchs)

                '''単語信頼度'''
                pattern2 = r'CM="(.*)"'
                data = re.findall(pattern2, recv_line[i])
                CM += data

                #単語ごとに文字を取り出すと最初と最後の要素が ""になる
                #単語が ""のとき信頼度は1になる
                #そのままだと ["", "りんご", "を", "食べる", ""] と言った形になるので
                #抜き出した単語ごとの文字列のリストから最初と最後の要素を消す
                #単語信頼度のリストも同様
                if "</SHYPO>" in recv_line[i]:
                    del matchs[0]
                    del matchs[len(matchs)-1]
                    del CM[0]
                    del CM[len(CM)-1]

                    CM_list.append(CM)
                    word_list.append(matchs)
                    CM = []

                    sentence_data.append(moji)
                    moji = ""
                    matchs = []

            '''尤度取り出し（juliusの結果全体から）'''
            pattern3 = r'SCORE="(.*)"'
            data = re.findall(pattern3, recv_data)
            if len(data) != 0:

                score_data += data

            if "</RECOGOUT>" in recv_data:
                break

        '''JSONファイルに書き込み'''
        obj = js.store(sentence_data, score_data, CM_list, word_list)

        """speech.jsonを送る"""
        host = "127.0.0.1"
        port = 5000

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #オブジェクトの作成をします

        client.connect((host, port)) #これでサーバーに接続します
        obj_sock = json.dumps(obj)

        client.send(obj_sock.encode('utf-8'))

        client.close()





if __name__ == '__main__':


    main()
