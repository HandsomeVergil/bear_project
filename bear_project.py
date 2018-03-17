from flask import Flask,jsonify
import requests

app=Flask(__name__)

@app.route('/')
def index():
    result=requests.get('https://search-maps.yandex.ru/v1/',params={'apikey':'4ad3e4de-10fa-4349-b95f-d4bf6e5524c2','text':'Пивная','lang':'ru_RU','ll':'55.4507,37.3656','spn':'0.552069,0.400552'})
    print(result.json())
    return jsonify(result.json())
if __name__ =='__main__':
    app.run()
index()
