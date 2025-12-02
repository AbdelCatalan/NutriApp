from flask import Flask, render_template, request, redirect, session
import json
import os

app = Flask(__name__)
app.secret_key = "stEtZjvtNMrhhvHYIH1u8g==SPcTTRHt2INatKcj"

def cargar_usuarios():
    if not os.path.exists("usuarios.json"):
        with open("usuarios.json", "w") as f:
            json.dump({}, f)
    with open("usuarios.json", "r") as f:
        return json.load(f)

def guardar_usuarios(usuarios):
    with open("usuarios.json", "w") as f:
        json.dump(usuarios, f, indent=4)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        usuario = request.form["usuario"]
        password = request.form["password"]
        usuarios = cargar_usuarios()
        if usuario in usuarios:
            return "El usuario ya existe"
        usuarios[usuario] = password
        guardar_usuarios(usuarios)
        return redirect("/login")
    return render_template("registro.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        password = request.form["password"]
        usuarios = cargar_usuarios()
        if usuario not in usuarios or usuarios[usuario] != password:
            return "Usuario o contraseña incorrectos"
        session["usuario"] = usuario
        return redirect("/")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect("/")

@app.route("/educacion")
def educacion():
    return render_template("educacion.html")

@app.route("/recetas")
def recetas():
    return render_template("recetas.html")

@app.route("/herramientas")
def herramientas():
    return render_template("herramientas.html")

@app.route("/macro", methods=["GET", "POST"])
def macro():
    resultado = None
    if request.method == "POST":
        peso = float(request.form["peso"])
        altura = float(request.form["altura"])
        edad = float(request.form["edad"])
        sexo = request.form["sexo"]

        if sexo == "hombre":
            calorias = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * edad)
        else:
            calorias = 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * edad)

        prote = peso * 2
        grasas = peso * 0.9
        carbs = (calorias - (prote * 4 + grasas * 9)) / 4

        resultado = {
            "calorias": round(calorias),
            "prote": round(prote),
            "carbs": round(carbs),
            "grasas": round(grasas)
        }
    return render_template("macro.html", resultado=resultado)

@app.route("/peso", methods=["GET", "POST"])
def peso():
    peso_ideal = None
    if request.method == "POST":
        altura = float(request.form["altura"])
        peso_ideal = round(50 + 0.75 * (altura - 150), 1)
    return render_template("peso.html", peso_ideal=peso_ideal)

@app.route("/imc", methods=["GET","POST"])
def imc():
    resultado = None
    categoria = None

    if request.method == "POST":
        peso = float(request.form["peso"])
        altura = float(request.form["altura"]) / 100

        imc_valor = peso / (altura ** 2)
        resultado = round(imc_valor, 2)

        if resultado < 18.5:
            categoria = "Bajo peso"
        elif resultado < 25:
            categoria = "Normal"
        elif resultado < 30:
            categoria = "Sobrepeso"
        else:
            categoria = "Obesidad"

    return render_template("imc.html", resultado=resultado, categoria=categoria)


@app.route("/gct", methods=["GET","POST"])
def gct():
    grasa = None

    if request.method == "POST":
        cintura = float(request.form["cintura"])
        peso = float(request.form["peso"])
        sexo = request.form["sexo"]

        if sexo == "hombre":
            grasa = ( (4.15 * cintura) - (0.082 * peso * 2.20462) - 98.42 ) / (peso * 2.20462) * 100
        else:
            grasa = ( (4.15 * cintura) - (0.082 * peso * 2.20462) - 76.76 ) / (peso * 2.20462) * 100

        grasa = round(grasa, 2)

    return render_template("gct.html", grasa=grasa)

@app.route("/tmb", methods=["GET","POST"])
def tmb():
    resultado = None

    if request.method == "POST":
        peso = float(request.form["peso"])
        altura = float(request.form["altura"])
        edad = float(request.form["edad"])
        sexo = request.form["sexo"]

        if sexo == "hombre":
            resultado = 10*peso + 6.25*altura - 5*edad + 5
        else:
            resultado = 10*peso + 6.25*altura - 5*edad - 161

        resultado = round(resultado, 2)

    return render_template("tmb.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
