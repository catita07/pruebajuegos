from flask import Flask, render_template, session, redirect, url_for, request
import random

app = Flask(__name__)
app.secret_key = 'tu clave secreta es esta' 

@app.route('/', methods=['GET'])
def juego():
    return render_template('juego.html')


@app.route('/enviar', methods=['POST'])
def enviar():
    nombre = request.form.get('nombre')    
    lugar = request.form.get('lugar')
    número = request.form.get('número')
    comida = request.form.get('comida')
    profesion = request.form.get('profesion')

    session['nombre'] = nombre
    session['lugar'] = lugar
    session['número'] = número
    session['comida'] = comida
    session['profesion'] = profesion

    return redirect(url_for('futuro'))


@app.route('/futuro', methods=['GET'] )
def futuro():
    nombre = session.get('nombre') 
    lugar = session.get('lugar')
    número = session.get('número')
    comida = session.get('comida')
    profesion = session.get('profesion')
    
    mensajes = [
        f"Soy el adivino del Dojo, {nombre} tendrá un viaje muy largo dentro de {número} años a {lugar} y estará el resto de sus días preparando {comida} para todas las personas que quiere.",
        f"Soy el adivino del Dojo, {nombre} tendrá {número} años de mala suerte, nunca conocerá {lugar} y jamás volvió a comer {comida}."
    ]
    mensaje = random.choice(mensajes)
    if profesion:
        mensaje += f" cambio de profesion y ahora es {profesion}." 

    return render_template('juego2.html', mensaje=mensaje)

if __name__=='__main__':
    app.run(debug=True)