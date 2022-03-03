# save this as app.py
from flask import Flask , render_template,url_for



var_app = Flask(__name__)

@var_app.route('/')
def inicio():
    return render_template('layout.html')
    
@var_app.route('/home')
def home():
    return render_template('home.html')

@var_app.route('/productos')
def productos():
    return render_template("productos.html")
   ### return render_template("index.html")

@var_app.route('/contactos')
def contactos():
    return render_template("contactos.html")
   ### return render_template("index.html")
@var_app.route('/q_somos')
def q_somos():
    return render_template("q_somos.html")
   ### return render_template("index.html")

@var_app.route('/ptotal')
def ptotal():
    return render_template('pTotal.html')

if __name__ == "__main__" :
    var_app.run(host='0.0.0.0',port=3000,debug=True,)




"""

if __name__ == "__main__" :
    var_app.run(debug=True,port=3000)

"""