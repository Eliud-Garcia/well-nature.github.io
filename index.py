from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/acerca')
def acerca():
    return render_template('acerca.html')

@app.route('/contactos')
def contactos():
    return render_template('contactos.html')

if __name__ == '__main__':
    app.run(debug=True)