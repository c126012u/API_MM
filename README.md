# API_MM
雑談APIとルールベース対話の統合

・MMD.py
 統合プログラム(認識結果を受け取って雑談システムへ)
 
・jtalk.py
  音声合成プログラム
  
・talk.py
   雑談APIプログラム
   
・
　ルールマッチプログラム
 
・julius.py
　音声認識をして結果を保存したJSONを統合プログラムへ送る
 
・
 画像から得られた情報（物体認識、動作認識）からID（input_scene.json）作成、統合プログラムへ送信
 
#flask_script_my
sk = {"skeleton":{SkLeftElbow_X 823
SkRightElbow_X 1121
SkLeftShoulder_Y 232
SkRightShoulder_Y 232
SkNeck_Y 154
SkRightHand_X 1132
SkLeftShoulder_X 895
SkHead_X 982
SkRightShoulder_X 1085
SkLeftHand_Y 226
SkHead_Y 50
SkRightElbow_Y 388
SkLeftHand_X 698
SkNeck_X 986
SkLeftElbow_Y 212
SkRightHand_Y 543}

scene.update(sk)
この行でscene.jsonを完成させたい
