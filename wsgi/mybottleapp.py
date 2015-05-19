from bottle import Bottle,route,default_app,request,template,static_file
from lxml import etree
import urllib2
import requests

@route('/')
def principal():
	return template("index.tpl")

@route('/busqueda',method='POST')
def localizacion():
	ubi=request.forms.get('ubicacion')
	url_base="https://maps.googleapis.com/maps/api/"
	dict={"address":ubi,"sensor":"false"}
	
	r=requests.get(url_base+"geocode/xml",params=dict)

	if r.status_code == 200:
		doc=etree.fromstring(r.text.encode("utf-8"))
		latitud=doc.find("result/geometry/location/lat").text

	return template("localizacion.tpl",lat=latitud,lon=longitud)

@route('/static/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='static')

# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/')) 

application=default_app()
