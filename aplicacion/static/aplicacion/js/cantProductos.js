function limpiarSiMenorOIgualCero() {
    var cantidadInput = document.getElementById('idcantidad');
    cantidadInput.value = cantidadInput.value.replace(/[^0-9]/g, ''); // Eliminar caracteres no deseados
    var cantidad = cantidadInput.value.trim(); // Eliminar espacios en blanco al inicio y al final
    var regex = /^[1-9]$/; // Expresión regular para aceptar solo un dígito entre 1 y 9

    if (!regex.test(cantidad)) {
        cantidadInput.value = ''; // Limpiar el campo si no cumple con la expresión regular
    }
}