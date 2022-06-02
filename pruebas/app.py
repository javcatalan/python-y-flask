from flask import Flask

app= Flask(__name__)

@app.route("/home")
@app.route("/")
def index():
    return "prueba"

@app.route("/contacto")
def contacto():
    return "<h1>contactanos</h1>"