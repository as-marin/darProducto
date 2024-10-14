document.addEventListener('DOMContentLoaded', function() {
    var telefonoInput = document.getElementById('id_telefono');
    if (telefonoInput) {
        telefonoInput.addEventListener('input', function() {
            this.value = this.value.replace(/[^0-9]/g, '').slice(0, 9);
        });
    }
});