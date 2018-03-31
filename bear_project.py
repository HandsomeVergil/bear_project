from flask import Flask, render_template, request,jsonify 
import requests 


my_flask_app=Flask(__name__)

@my_flask_app.route('/')
def index():
    return render_template('index1.html')
@my_flask_app.route('/main')
def api_acces():
    result=requests.get('https://search-maps.yandex.ru/v1/',params={'apikey':'4ad3e4de-10fa-4349-b95f-d4bf6e5524c2','text':'Пивная','lang':'ru_RU','ll':'37.618920,55.756994','spn':'0.552069,0.400552'})
    #print(result.text.encode('utf-8'))
    for value in result.json()['features']:
    	properties=value['properties']
    	print(properties['name'])
    return jsonify(result.json())


if __name__=='__main__':
    my_flask_app.run()
 

