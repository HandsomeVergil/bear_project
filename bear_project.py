from flask import Flask, render_template, request,jsonify 
import requests 


my_flask_app=Flask(__name__)

@my_flask_app.route('/')
def index():
    return render_template('index1.html')
@my_flask_app.route('/main')
def api_acces():
    result=requests.get('https://search-maps.yandex.ru/v1/',params={'apikey':'4ad3e4de-10fa-4349-b95f-d4bf6e5524c2','text':'Пивная','lang':'ru_RU',
    	'bbox':'36.83,55.50~38.24,55.91',
    	'results':'420'
    	#'ll':'37.618920,55.756994',
    	#'spn':'0.552069,0.400552'
    	})
    #print(result.text.encode('utf-8'))
    d_result=result.json()
    features=[]
    _id=0
    my_list=[]
    for geom in d_result['features']:
    	geometry=geom['geometry']
    	coordinates=geometry['coordinates']
    	x,y=coordinates
    	#print(x,',',y)
    	name=geom['properties']['name']
    	my_list.append({'name':name,'x':x,'y':y})
    	features.append( {
        "type": "Feature", 
        "id": _id, 
        "geometry": {"type": "Point", "coordinates": [y,x]},
         "properties": {"clusterCaption": "<strong> %s </strong>" %name}
         })
    	print(name,x,y)
    	_id+=1
    print(len(d_result['features']))

    #return render_template('coor_name.html', my_list=my_list)
    #return jsonify(d_result)
    return jsonify({
    "type": "FeatureCollection",
    "features": features})
@my_flask_app.route('/coor_name')
def coor_name():
    return render_template('coor_name.html' )


@my_flask_app.route('/barlist')
def bar_list():
    barlist=[]
    result=requests.get('https://search-maps.yandex.ru/v1/',params={'apikey':'4ad3e4de-10fa-4349-b95f-d4bf6e5524c2','text':'Пивная','lang':'ru_RU',
        'bbox':'36.83,55.50~38.24,55.91',
        'results':'420'
        #'ll':'37.618920,55.756994',
        #'spn':'0.552069,0.400552'
        })
    #print(result.text.encode('utf-8'))
    d_result=result.json()
    for geom in d_result['features']:
        geometry=geom['geometry']
        coordinates=geometry['coordinates']
        x,y=coordinates
        #print(x,',',y)
        name=geom['properties']['name']
        barlist.append(name)

    return render_template('barlist.html', barlist=barlist)


if __name__=='__main__':
    my_flask_app.run(debug=True)
 


