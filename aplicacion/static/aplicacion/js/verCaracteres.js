function limpiarCaracteres() {
    var cantidadInput = document.getElementById('idnombreProducto');
    cantidadInput.value = cantidadInput.value.replace(/[^a-zA-Z0-9\s]/g, ''); // Eliminar caracteres no deseados excepto letras, números y espacios en blanco
    var cantidad = cantidadInput.value.trim(); // Eliminar espacios en blanco al inicio y al final

    if (!/^[a-zA-Z0-9\s]*$/.test(cantidad)) {
        cantidadInput.value = ''; // Limpiar el campo si no cumple con la expresión regular
    }
}

