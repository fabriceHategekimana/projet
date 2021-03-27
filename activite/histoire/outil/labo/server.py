from cmd import Cmd
from mycompile import *
import re
import csv

import json
from flask import Flask, jsonify, request
app = Flask(__name__)

white= ["file:///home/fabrice/projet/activite/histoire/outil/labo/network.html"]

@app.route('/', methods=['POST'])
def hello_world():
   print("request: ", request.data);
   #inp = json.loads(request.data)
   #parser.parse(inp)
   #return jsonify(union(request.data))
   return jsonify(request.data)

@app.after_request
def add_cors_headers(response):
    r = request.referrer[:-1]
    if r in white:
        response.headers.add('Access-Control-Allow-Origin', r)
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Headers', 'Cache-Control')
        response.headers.add('Access-Control-Allow-Headers', 'X-Requested-With')
        response.headers.add('Access-Control-Allow-Headers', 'Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE')
    return response

if __name__ == '__main__':
   app.run()
