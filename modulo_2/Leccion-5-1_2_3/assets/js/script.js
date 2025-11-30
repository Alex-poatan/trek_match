// Obtener el botón "Ir arriba"
const scrollToTopBtn = document.getElementById('scrollToTop');

// Función para hacer smooth scroll hacia arriba
function scrollToTop() {
    // window.scrollTo() hace scroll a una posición específica
    // { top: 0 } significa ir al inicio (posición 0)
    // { behavior: 'smooth' } hace que el scroll sea suave (animado)
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

// Añadir evento click al botón
scrollToTopBtn.addEventListener('click', scrollToTop);

console.log('Script JavaScript cargado correctamente: Smooth scroll activo');
