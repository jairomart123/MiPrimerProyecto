from distutils.log import debug
from flask import flask

var_app = flask(__name__)



if __name__ == "__main__":
    var_app.raun(debug=True,port=3000)
