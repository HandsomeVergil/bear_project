from flask import Flask,jsonify
import requests

app=Flask(__name__)

@app.route('/')
def index():
    result=requests.get('https://search-maps.yandex.ru/v1/',params={'apikey':'4ad3e4de-10fa-4349-b95f-d4bf6e5524c2','text':'Пивная','lang':'ru_RU'})
    print(result.json())
    return jsonify(result.json())
if __name__ =='__main__':
    app.run()
index()
