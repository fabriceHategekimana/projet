from cmd import Cmd
from mycompile import *
import re
import csv

import json
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello_world():
   inp = json.loads(request.data)
   #parser.parse(inp)
   return jsonify(union(inp))

if __name__ == '__main__':
   app.run()
