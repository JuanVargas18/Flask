from flask import Flask, request, render_template
from markupsafe import escape
app = Flask(__name__)

@app.get("/")
def hola_mundo():
    return render_template("index.html", )

    
@app.get("/bienvenida")
def bienvenida():
    return render_template("bienvenida.html", nombre=nombre())

def nombre():
    return request.args.get("nombre", "mundo")