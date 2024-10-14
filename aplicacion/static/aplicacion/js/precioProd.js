function precioprod() {
    var cantidadInput = document.getElementById('idprecioProducto');
    if (!cantidadInput) {
        console.error("El elemento con el ID 'idprecioProducto' no existe.");
        return;
    }

    // Eliminar caracteres no deseados y limitar la entrada a un máximo de 6 dígitos
    cantidadInput.value = cantidadInput.value.replace(/\D/g, '').slice(0, 6);
    var cantidad = cantidadInput.value.trim(); // Eliminar espacios en blanco al inicio y al final

    var regex = /^[1-9]\d*$/; // Expresión regular para aceptar números enteros positivos (mínimo 1 dígito)

    if (!regex.test(cantidad)) {
        cantidadInput.value = ''; // Limpiar el campo si no cumple con la expresión regular
    }
}
