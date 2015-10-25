from flask import Flask
from flask.ext.cors import CORS

app = Flask(__name__)
CORS(app)

import ymir.api
