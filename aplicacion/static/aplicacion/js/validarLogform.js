document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('loginForm').addEventListener('submit', function(event) {
        var rutCompleto = document.getElementById('idrutini').value;
        if (!Fn.validaRut(rutCompleto)) {
            event.preventDefault(); // Evita que se envíe el formulario si el RUT es inválido
            alert("El RUT ingresado es inválido. Por favor, ingrese un RUT válido.");
        }
    });
});