from flask import Flask

var_app = Flask(__name__)

@var_app.route("/")

def inicio():
    return"Hola mundo"

@var_app.route("/cur")

def cur():
    return"Bienvenido a la univercidad"

if __name__ == "__main__":
    var_app.run(debug=True,port=3000)

