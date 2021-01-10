import os
import sys
import json

import requests
from flask import Flask, jsonify, render_template, request
from predict import getPrediction
app = Flask(__name__)

@app.route('/', methods=['POST'])
def json():
    url = "chatfuel_api"
    data = json.load(urllib2.urlopen(url))

    if request.json:
        mydata = request.json
        res = getPrediction(mydata)  
        return res

    else:
        return "no json received"
if __name__ == '__main__':
    app.run(debug=True)