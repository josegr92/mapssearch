from bottle import Bottle,route,default_app,request,template,static_file
from lxml import etree
import urllib2
import requests

@route('/')
def principal():
	return template("index.tpl")

@route('/busqueda',method='POST')
def localizacion():
	clave="AIzaSyAGPVr0-l9x0Lowgw8e39Ett8fNpuTTxI0"
	ubi=request.forms.get('ubicacion')
	lug=request.forms.get('lugar')
	url_base="https://maps.googleapis.com/maps/api/"
	dict={"address":ubi,"sensor":"false"}
	
	r=requests.get(url_base+"geocode/xml",params=dict)

	if r.status_code == 200:
		doc=etree.fromstring(r.text.encode("utf-8"))
		latitud=doc.find("result/geometry/location/lat").text
		longitud=doc.find("result/geometry/location/lng").text
		lat_long=str(latitud)+","+str(longitud)
		dict2={"location":lat_long,"language":"es","radius":"3000","types":lug,"sensor":"false","key":clave}
		r2=requests.get(url_base+"place/nearbysearch/xml",params=dict2)

		if r2.status_code == 200:
			doc2=etree.fromstring(r2.text.encode("utf-8"))
			resultados=doc2.findall("result")
			localizacion=[]
			for resultado in resultados:
				loc=[]
				nombre=resultado.find("name").text
				latitud2=float(resultado.find("geometry/location/lat").text)
				longitud2=float(resultado.find("geometry/location/lng").text)
				loc.append(nombre.encode("utf-8"))
				loc.append(latitud2)
				loc.append(longitud2)
				localizacion.append(loc)

	return template("localizacion.tpl",lat=localizacion)


@route('/static/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='static')

# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/')) 

application=default_app()
