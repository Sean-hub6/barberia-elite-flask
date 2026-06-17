

let total = 0;

function agregarReserva(servicio, precio, idFecha, idHora){
    const fecha = document.getElementById(idFecha).value;
    const hora = document.getElementById(idHora).value;

    const reserva = {
        servicio: servicio,
        precio: precio,
        fecha: fecha,
        hora: hora
    };

    fetch("/api/reserva", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(reserva)
    });

    alert("Reserva enviada al sistema 💈");
}

function limpiarReservas(){

    document.getElementById("listaReservas").innerHTML = "";

    total = 0;

    document.getElementById("total").textContent = total;
}


