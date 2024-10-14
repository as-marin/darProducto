function validarEdad() {
    var fechaNacimiento = new Date(document.getElementById("fechaNacimiento").value);
    var edadMessage = document.getElementById("edadMessage");
    
    // Calcular la fecha actual
    var fechaActual = new Date();
    
    // Calcular la edad en milisegundos
    var edadEnMs = fechaActual - fechaNacimiento;
    
    // Convertir la edad en milisegundos a años
    var edadEnAnios = Math.floor(edadEnMs / 31557600000); // 31557600000 ms = 1 año
    
    if (edadEnAnios < 18) {
        edadMessage.innerHTML = "Debe ser mayor de 18 años para registrarse.";
        document.getElementById("fechaNacimiento").value = ''; // Limpiar el campo de fecha de nacimiento
    } else {
        edadMessage.innerHTML = "";
    }
}