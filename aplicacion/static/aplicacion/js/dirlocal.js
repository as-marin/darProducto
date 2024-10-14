
document.addEventListener('DOMContentLoaded', function() {
    // Obtener los elementos de los campos de entrega
    var direccionInput = document.getElementById('direccion');
    var deptInput = document.getElementById('dept');

    // Cargar valores guardados del LocalStorage al cargar la página
    direccionInput.value = localStorage.getItem('direccion') || '';
    deptInput.value = localStorage.getItem('dept') || '';

    // Guardar valores al cambiar los campos
    direccionInput.addEventListener('input', function() {
        localStorage.setItem('direccion', direccionInput.value);
    });

    deptInput.addEventListener('input', function() {
        localStorage.setItem('dept', deptInput.value);
    });
});

