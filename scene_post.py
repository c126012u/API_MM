import urllib.request, json
import base64

def convert_b64(file_path):
    """
    b64にエンコード
    """
    return base64.encodestring(open(file_path, 'rb').read()).decode("utf-8")

if __name__ == '__main__':
    #送信先
    #post_request
    url = "http://127.0.0.1:5000/scene"

    method = "POST"
    headers = {"Content-Type" : "application/json"}

    obj = {
            "20":{
                "locaton":["x", "y", "z"],
                "motion":"POINTING",
                "name":[
                    "ねこ",
                    "いぬ",
                    "エルモ",
                    "ピカチュウ",
                    "トトロ"
                ],
                "confidence":[
                    "50.0",
                    "16.0",
                    "14.0",
                    "11.0",
                    "9.0"
                ]
            },
            "11":{
                "locaton":["x", "y", "z"],
                "motion":"",
                "name":[
                    "いぬ",
                    "エルモ",
                    "トトロ",
                    "ねこ",
                    "ピカチュウ"
                ],
                "confidence":[
                    "60.0",
                    "20.0",
                    "17.0",
                    "15.0",
                    "10.0"
                ]
            }

        }

    json_data = json.dumps(obj).encode("utf-8")
    # httpリクエストを準備してPOST
    request = urllib.request.Request(url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode("utf-8")
