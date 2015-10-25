from flask import Flask
from flask.ext.cors import CORS

__version__ = '0.0.1'

app = Flask(__name__)
CORS(app)

import ymir.api

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
