from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

reservas = []

@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    total = len(reservas)
    ingresos = sum(r["precio"] for r in reservas)

    return render_template(
        "dashboard.html",
        reservas=reservas,
        total=total,
        ingresos=ingresos
    )


@app.route("/api/reserva", methods=["POST"])
def api_reserva():

    data = request.json

    reservas.append({
        "fecha": data["fecha"],
        "hora": data["hora"],
        "servicio": data["servicio"],
        "precio": data["precio"]
    })

    return jsonify({"mensaje": "ok"})