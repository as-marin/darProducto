function limpiarSoloNumeros(inputId) {
    var input = document.getElementById(inputId);
    if (!input) {
        console.error("El elemento con el ID especificado no existe.");
        return;
    }

    input.addEventListener('input', function() {
        var valor = this.value;
        var newValue = '';

        for (var i = 0; i < valor.length; i++) {
            if (/[0-9]/.test(valor[i])) {
                newValue += valor[i];
            }
        }

        this.value = newValue;
    });
}