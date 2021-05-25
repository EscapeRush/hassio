#!/usr/bin/env python

import requests
#from requests import get
import urllib
import json
import os
import random

from flask import Flask, request, jsonify
from flask_sslify import SSLify  
from flask_cors import CORS, cross_origin

  

token=""

try:
    f = open('token.txt', 'r')
    
except :
    
    print('cannot opentoken.txt ')

else:
    token=f.read().rstrip()
    f.close()

#urlhomeassistant = "http://127.0.0.1:8123"
#urlhomeassistant = "http://192.168.1.75:8123"
#urlhomeassistant = "http://homeassistant.local:8123"
#urlhomeassistant = "http://localhost:8123"
ip=""
try:
    f = open('ipconfig.txt', 'r')
    
except :
    
    print('mettre adresse ip du raspberry dans fichier ipconfig.txt ')

else:
    ip=f.read().rstrip()
    f.close()

urlhomeassistant = "https://"+ip+":8123"
print("url homeassistant : "+urlhomeassistant)

headers = {"Authorization": "Bearer "+token,"content-type": "application/json",}

 

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'




@app.route('/api/webhook/<webhook_id>', methods=['GET'])
@cross_origin()
def triger(webhook_id):
    print("rx /api/webhook/ for "+webhook_id)
    
    url=urlhomeassistant+'/api/webhook/'+webhook_id
    response =requests.post(url)
    
    return 'request send to automation with webhookid = '+webhook_id


@app.route('/textapi/states/<sensorid>', methods=['GET'])
@cross_origin()
def states(sensorid):
    print("rx textapi/states/ for "+sensorid)
    
    url=urlhomeassistant+'/api/states/'+sensorid
    response = requests.get(url, headers=headers, verify=False)
    reponsejson=response.json()
    try:
        url=urlhomeassistant+'/api/states/'+sensorid
        response = requests.get(url, headers=headers, verify=False)
        reponsejson=response.json()
        return reponsejson['state']
    except:
        return 'error for '+sensorid
    
@app.route('/', methods=['GET'])
@cross_origin()
def test():
    print("rx / ")
    return 'hello ' 

if __name__ == "__main__":
    app.run(host= '0.0.0.0',port=8000)
   
context = ('rv.crt', 'rv.key') #il faut mettre tes certificats dans le dossier
sslify = SSLify(app)
app.run(host= '0.0.0.0',port=8000,ssl_context = context)
    

