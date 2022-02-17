from flask import Flask , render_template

var_app = Flask(__name__)

@var_app.route("/")

def inicio():
    return"Hola mundo"

@var_app.route("/cur")

def cur():
    return render_template("/Cur.html")
    

if __name__ == "__main__" :
    var_app.run(debug=True,port=3000)

##if __name__ == "__main__" :
    ##var_app.run(host='0.0.0.0',port=3000,debug=True,)
