

let total = 0;

function agregarReserva(servicio, precio, idFecha, idHora){

    let fecha = document.getElementById(idFecha).value;
    let hora = document.getElementById(idHora).value;

    let lista = document.getElementById("listaReservas");

    let item = document.createElement("li");

    item.textContent =
        servicio +
        " | Fecha: " + fecha +
        " | Hora: " + hora +
        " | S/ " + precio;

    lista.appendChild(item);

    total += precio;

    document.getElementById("total").textContent = total;
}

function limpiarReservas(){

    document.getElementById("listaReservas").innerHTML = "";

    total = 0;

    document.getElementById("total").textContent = total;
}


