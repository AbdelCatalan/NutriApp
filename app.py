from flask import Flask, render_template_string, request

app = Flask(__name__)

# Página principal
@app.route('/')
def inicio():
    return """
    <html>
    <head>
      <meta charset='UTF-8'>
      <title>NutriApp</title>
      <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css' rel='stylesheet'>
      <style>
        body { background: #f2f9f1; font-family: Arial; }
        .navbar { background-color: #6ab04c; }
        footer { text-align:center; margin-top:30px; padding:15px; background:#6ab04c; color:white; }
      </style>
    </head>
    <body>
      <nav class='navbar navbar-expand-lg navbar-dark'>
        <div class='container-fluid'>
          <a class='navbar-brand' href='/'>NutriApp</a>
          <ul class='navbar-nav'>
            <li class='nav-item'><a class='nav-link active' href='/'>Inicio</a></li>
            <li class='nav-item'><a class='nav-link' href='/formulario'>Registro</a></li>
          </ul>
        </div>
      </nav>

      <div class='container mt-4 text-center'>
        <h3 class='text-success'>Bienvenido a NutriApp</h3>
        <p class='text-muted'>Plantilla base del diseño de la app nutricional.</p>
      </div>

      <footer>NutriApp 2025 - Prototipo visual</footer>
    </body>
    </html>
    """

# Página de formulario
@app.route('/formulario')
def formulario():
    return """
    <html>
    <head>
      <meta charset='UTF-8'>
      <title>Registro</title>
      <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css' rel='stylesheet'>
      <style>
        body { background: #f2f9f1; font-family: Arial; }
        .navbar { background-color: #6ab04c; }
        footer { text-align:center; margin-top:30px; padding:15px; background:#6ab04c; color:white; }
      </style>
    </head>
    <body>
      <nav class='navbar navbar-expand-lg navbar-dark'>
        <div class='container-fluid'>
          <a class='navbar-brand' href='/'>NutriApp</a>
          <ul class='navbar-nav'>
            <li class='nav-item'><a class='nav-link' href='/'>Inicio</a></li>
            <li class='nav-item'><a class='nav-link active' href='/formulario'>Registro</a></li>
          </ul>
        </div>
      </nav>

      <div class='container mt-4'>
        <div class='card shadow p-4'>
          <h3 class='text-center text-success'>Registro de Alimentación Diaria</h3>
          <form action='/resultado' method='post'>
            <div class='mb-3'>
              <label>Nombre:</label>
              <input type='text' name='nombre' class='form-control' placeholder='Tu nombre'>
            </div>
            <div class='mb-3'>
              <label>Comida que consumiste:</label>
              <input type='text' name='comida' class='form-control' placeholder='Ejemplo: Ensalada con pollo'>
            </div>
            <div class='mb-3'>
              <label>Calorías aproximadas:</label>
              <input type='number' name='calorias' class='form-control' placeholder='Ejemplo: 450'>
            </div>
            <button type='submit' class='btn btn-success w-100'>Guardar</button>
          </form>
        </div>
      </div>

      <footer>NutriApp 2025 - Diseño de muestra</footer>
    </body>
    </html>
    """

# Página de resultado
@app.route('/resultado', methods=['POST'])
def resultado():
    nombre = request.form.get("nombre", "Desconocido")
    comida = request.form.get("comida", "Sin datos")
    calorias = request.form.get("calorias", "0")

    return f"""
    <html>
    <head>
      <meta charset='UTF-8'>
      <title>Resultado</title>
      <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css' rel='stylesheet'>
      <style>
        body {{ background: #f2f9f1; font-family: Arial; }}
        .navbar {{ background-color: #6ab04c; }}
        footer {{ text-align:center; margin-top:30px; padding:15px; background:#6ab04c; color:white; }}
      </style>
    </head>
    <body>
      <nav class='navbar navbar-expand-lg navbar-dark'>
        <div class='container-fluid'>
          <a class='navbar-brand' href='/'>NutriApp</a>
        </div>
      </nav>

      <div class='container mt-5'>
        <div class='card shadow p-4 text-center'>
          <h4>Resultado del Registro</h4>
          <p><b>Nombre:</b> {nombre}</p>
          <p><b>Comida:</b> {comida}</p>
          <p><b>Calorías:</b> {calorias}</p>
          <p class='text-muted mt-3'>Solo formato visual (sin base de datos).</p>
          <a href='/formulario' class='btn btn-primary'>Regresar</a>
        </div>
      </div>

      <footer>NutriApp 2025 - Ejemplo visual</footer>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
