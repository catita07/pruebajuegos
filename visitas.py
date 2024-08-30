from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'tu clave secreta es esta' 

@app.route('/')
def visitass():
    if 'visitas' not in session:
        session['visitas'] = 1
        session['reinicios'] = 0
    else:
        session['visitas'] += 1
    return render_template('visitass.html', visitas=session['visitas'], reinicios=session['reinicios'])

@app.route('/destruir_sesion')
def destruir_sesion():
    session.clear()
    return redirect(url_for('visitass'))

@app.route('/sumar_dos')
def sumar_dos():
    session['visitas'] += 2
    return redirect(url_for('visitass'))

@app.route('/reiniciar')
def reiniciar():
    session['visitas'] = 0
    session['reinicios'] += 1
    return redirect(url_for('visitass'))

@app.route('/sumar_valor', methods=['POST'])
def sumar_valor():
    valor = int(request.form['valor'])
    session['visitas'] += valor
    return redirect(url_for('visitass'))

if __name__ == '__main__':
    app.run(debug=True)