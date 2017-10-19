from flask import Flask,request,jsonify
import base64
import re

#リクエストを受けたらscene.json（尤度と名前以外）を送るように書き換え
#参考： http://uokada.hatenablog.jp/entry/2012/11/10/002453

#server
app = Flask(__name__)

def convert_b64_to_file(b64,outfile_path):
    """
    b64をデコードしてファイルに書き込む
    """
    s = base64.decodestring(b64)
    with open(outfile_path,"wb") as f :
        f.write(s)

@app.route("/")
def index():
    return "send me json hello "

#base64でエンコードされたjsonファイルをデコード
@app.route('/post_request', methods=['POST'])
def post_request():
    # Bad request
    if not request.headers['Content-Type'] == 'application/json':
        return jsonify(res='failure'), 400
    ###jsonはdict型なので即変換できないからlistに入れて処理している

    #jsonを取得
    data = request.json
    #keysを取得
    keys_array = list(data.keys())
    #valuesを取得
    values_array = list(data.values())
    """
    送ってくるjsonは一つ目の要素が{画像名:base64エンコード}としたもの
    """
    # print(keys_array)
    # print(type(keys_array))
    # print(type(keys_array[0]))
    #fは、IDが保存されたファイル
    f=open("ID_list.txt","w")
    ske=open("sk.txt","w")
    #IDソート用のlist
    IDlist=[]
    #depth用のlist
    depthlist=[]
    xmin=[]
    xmax=[]
    ymin=[]
    ymax=[]
    #keys_arrayにあるkeyリストをひとつひとつ見ていく
    f.write("ID\tPointing\tDepth\tXmax\tYmax\tXmin\tYmin\n-------------------------------------------------------------\n")
    for key_index in range(len(keys_array)):

        """
        ここでJSONkeyの場合分けをしている
        """

        #画像だった場合
        if re.search("Objects",keys_array[key_index]):
            object_name = []
            confidence = []
            '''
            object_name[0]:ID1の物体名N-best
            object_name[1]:ID2の物体名N-best
            ...
            confidence[0]~も同様
            '''
            #画像の保存名
            save_name = keys_array[key_index] + ".jpg"
            #コンバート
            convert_b64_to_file(bytes(values_array[key_index],"utf-8"),save_name)

            '''
            切り出し画像を、物体認識プログラムへ入力
            ここで物体辞書を用意
            '''

        #ID番号が入っている場合
        elif re.search("ObjectID",keys_array[key_index]):
            #IDlistに追加
            IDlist.append(int(keys_array[key_index][0]))
            #ソート
            IDlist=sorted(IDlist)
        elif re.search("ObjectDepth",keys_array[key_index]):
            depthlist.append([int(keys_array[key_index][0]),int(values_array[key_index])])
        elif re.search("Pointing",keys_array[key_index]):
            point=int(keys_array[key_index][0])
        elif re.search("Sk",keys_array[key_index]):
            ske.write(str(keys_array[key_index])+" "+str(values_array[key_index])+"\n")

        elif re.search("Xmax",keys_array[key_index]):
            xmax.append([int(keys_array[key_index][0]),int(values_array[key_index])])
        elif re.search("Xmin",keys_array[key_index]):
            xmin.append([int(keys_array[key_index][0]),int(values_array[key_index])])
        elif re.search("Ymax",keys_array[key_index]):
            ymax.append([int(keys_array[key_index][0]),int(values_array[key_index])])
        elif re.search("Ymin",keys_array[key_index]):
            ymin.append([int(keys_array[key_index][0]),int(values_array[key_index])])
        #それ以外の場合は空文字を表示
        else:
            print("",end="")
    #ここに関しては即興
    #file_str=""
    '''
    IDlist=[]
    depthlist=[]
    xmin=[]
    xmax=[]
    ymin=[]
    ymax=[]
    '''

    '''データ等格納'''
    scene = cl.OrderedDict()#順番にデータ格納するため
    for i in range(len(IDlist)):
        data = cl.OrderedDict()#順番にデータ格納するため
        data["location"] = [i]
        data["motion"] = [i]
        data["object"] = [i]
        data["confidence"] = [i]


        ys[sentence_list[i]] = data #辞書型のデータ
    ###
    scene = cl.OrderedDict()#順番にデータ格納するため
    for i in IDlist:
        data = cl.OrderedDict()#順番にデータ格納するため
        if i == point:
            data["motion"] = "POINTING"
        else:
            data["motion"] = ""
        for j in depthlist:
            if j[0] == i:
                j[1]
        for j in xmax:
            if j[0] == i:
                f.write(str(j[1])+"\t")
        for j in ymax:
            if j[0] == i:
                f.write(str(j[1])+"\t")
        for j in xmin:
            if j[0] == i:
                f.write(str(j[1])+"\t")
        for j in ymin:
            if j[0] == i:
                f.write(str(j[1]))
    ###

    data.update(skeleton)
    fs = open('sentence.json','w')
    fl = open('sentence_log.json', 'a+')

    json.dump(ys,fs,indent=4,ensure_ascii=False)
    json.dump(ys,fl,indent=4,ensure_ascii=False)

    return jsonify(res='success', **data)

##発話の認識結果のjsonを保存する
@app.route('/chat', methods=['POST'])
def post_request_chat():
    # Bad request
    if not request.headers['Content-Type'] == 'application/json':
        return jsonify(res='failure'), 400
    ###jsonはdict型なので即変換できないからlistに入れて処理している

    #jsonを取得
    data = request.json
    #keysを取得
    keys_array = list(data.keys())
    #valuesを取得
    values_array = list(data.values())
    """
    送ってくるjsonはN_bestで作ったやつ
    """
    #とりあえず会話文とスコアをprintしてみる
    #values_array
    for i in range(len(keys_array)):
        print(values_array[i]["sentence"],values_array[i]["score"])

    #会話文と尤度


    return jsonify(res='success', **data)


if __name__ == "__main__":
    app.debug = True
    #app.run(host = "163.225.223.101")
    app.run(host = "0.0.0.0")
