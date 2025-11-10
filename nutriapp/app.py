from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

usuarios = []

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/perfil', methods=['GET', 'POST'])
def perfil():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        email = request.form['email']
        password = request.form['password']
        edad = request.form.get('edad')
        sexo = request.form.get('sexo')
        objetivo = request.form.get('objetivo')

        print(f"Nuevo perfil creado: {nombre} {apellidos}, {email}, {edad} años, {sexo}, Objetivo: {objetivo}")

        return render_template('perfil.html', mensaje="Perfil registrado correctamente ")
    return render_template('perfil.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if email == 'usuario@correo.com' and password == '1234':
            return redirect(url_for('perfil'))
        else:
            error = "Correo o contraseña incorrectos"
            return render_template('login.html', error=error)

    return render_template('login.html')

@app.route('/educacion')
def educacion():
    return render_template('educacion.html')

@app.route('/recetas')
def recetas():
    return render_template('recetas.html')

@app.route('/herramientas')
def herramientas():
    return render_template('herramientas.html')

if __name__ == '__main__':
    app.run(debug=True)