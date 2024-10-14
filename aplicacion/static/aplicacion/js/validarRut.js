document.addEventListener('DOMContentLoaded', function() {
    var rutInput = document.getElementById('rut');
    if (rutInput) {
        rutInput.addEventListener('blur', function() {
            var rutValue = rutInput.value;
            Fn.validaRut(rutValue);
        });
    }
});

var Fn = {
    // Valida el rut con su cadena completa "XXXXXXXX-X"
    validaRut: function(rutCompleto) {
        var messageElement = document.getElementById("rutMessage");

        if (!/^[0-9]+[-|‐]{1}[0-9kK]{1}$/.test(rutCompleto)) {
            if (messageElement) {
                messageElement.innerHTML = "El RUT ingresado es inválido.";
            }
            return false;
        }
        
        var tmp = rutCompleto.split('-');
        var digv = tmp[1];
        var rut = tmp[0];
        if (digv == 'K') digv = 'k';
        if (Fn.dv(rut) == digv) {
            // El RUT es válido
            if (messageElement) {
                messageElement.innerHTML = "El RUT ingresado es válido.";
            }
            return true;
        } else {
            // El RUT es inválido
            if (messageElement) {
                messageElement.innerHTML = "El RUT ingresado es inválido.";
            }
            return false;
        }
    },
    dv: function(T) {
        var M = 0,
            S = 1;
        for (; T; T = Math.floor(T / 10))
            S = (S + T % 10 * (9 - M++ % 6)) % 11;
        return S ? S - 1 : 'k';
    }
};
