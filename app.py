from flask import Flask, render_template, request, jsonify, redirect, session

app = Flask(__name__)
app.secret_key = "barberiaelite2026"

reservas = []
usuarios = []

@app.route("/")
def inicio():
    if "usuario" not in session:
        return redirect("/login")

    return render_template("index.html", usuario=session["usuario"])


@app.route("/dashboard")
def dashboard():

    total = len(reservas)
    ingresos = sum(r["precio"] for r in reservas)

    clientes = len(usuarios)
    productos = 42

    dias = ["Lun","Mar","Mié","Jue","Vie","Sáb","Dom"]
    ventas = [10,6,6,9,12,10,7]

    return render_template(
        "dashboard.html",
        reservas=reservas,
        total=total,
        ingresos=ingresos,
        clientes=clientes,
        productos=productos,
        dias=dias,
        ventas=ventas
    )


@app.route("/api/reserva", methods=["POST"])
def api_reserva():

    data = request.json

    reservas.append({
        "nombre": data["nombre"],
        "fecha": data["fecha"],
        "hora": data["hora"],
        "servicio": data["servicio"],
        "precio": data["precio"]
    })

    return jsonify({"mensaje": "ok"})

@app.route("/borrar/<int:index>")
def borrar(index):
    reservas.pop(index)
    return redirect("/dashboard")

@app.route("/login", methods=["GET", "POST"])
def login():
    mensaje = ""

    if request.method == "POST":
        correo = request.form["correo"]
        password = request.form["password"]

        for usuario in usuarios:
            if usuario["correo"] == correo and usuario["password"] == password:
                session["usuario"] = usuario["nombre"]
                return redirect("/")

        mensaje = "Correo o contraseña incorrectos"

    return render_template("login.html", mensaje=mensaje)


@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nombre = request.form["nombre"]
        correo = request.form["correo"]
        password = request.form["password"]

        usuarios.append({
            "nombre": nombre,
            "correo": correo,
            "password": password
        })

        return redirect("/login")

    return render_template("registro.html")


@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect("/login")



if __name__ == "__main__":
    print("Estoy entrando al main...")
    app.run(debug=True)