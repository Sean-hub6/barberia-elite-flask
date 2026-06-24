

let total = 0;

function agregarReserva(servicio, precio, idFecha = null, idHora = null){
    const nombre = document.getElementById("nombreCliente").value;
    let fecha = "";
    let hora = "";

    if(idFecha){
        fecha = document.getElementById(idFecha).value;
    }

    if(idHora){
        hora = document.getElementById(idHora).value;
    }

    const reserva = {
        nombre: nombre,
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
    })
    .then(() => {
        alert("Reserva enviada al sistema 💈");
        window.location.href = "/dashboard";
    });
}

function limpiarReservas(){

    document.getElementById("listaReservas").innerHTML = "";

    total = 0;

    document.getElementById("total").textContent = total;
}


