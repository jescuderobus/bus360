function showHelpModal() {
    document.getElementById('customPopup').style.display = 'none'; // Oculta el menú
    document.getElementById('helpModal').style.display = 'block'; // Muestra el modal
}

// Cierra el modal cuando se hace clic en el botón de cerrar
document.querySelector('.close').onclick = function() {
    document.getElementById('helpModal').style.display = 'none';
    document.querySelector('.menu').style.display = 'block'; // Muestra el menú nuevamente
}

// Cierra el modal cuando se hace clic fuera del contenido del modal
window.onclick = function(event) {
    if (event.target == document.getElementById('helpModal')) {
        document.getElementById('helpModal').style.display = 'none';
        document.querySelector('.menu').style.display = 'block'; // Muestra el menú nuevamente
    }
}