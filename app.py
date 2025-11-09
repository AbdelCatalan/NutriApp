from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

usuarios = []

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/perfil', methods=['GET', 'POST'])
def perfil():
    if request.method == 'POST':
        email = request.form.get('email')
        if any(u['email'] == email for u in usuarios):
            return redirect(url_for('perfil'))  # Si ya existe, vuelve a la página
        else:
            usuarios.append({
                'nombre': request.form.get('nombre'),
                'apellidos': request.form.get('apellidos'),
                'email': email
            })
            return redirect(url_for('inicio'))
    return render_template('perfil.html')

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