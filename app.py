from flask import Flask, render_template, request, jsonify, redirect

app = Flask(__name__)

reservas = []

@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():

    total = len(reservas)
    ingresos = sum(r["precio"] for r in reservas)

    clientes = 25
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
