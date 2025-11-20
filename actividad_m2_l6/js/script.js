// ============================================
// SCRIPT PRINCIPAL - actividad_m2_l6
// ============================================

// $(document).ready() espera a que el DOM esté completamente cargado
$(document).ready(function() {
    console.log('✓ jQuery cargado y DOM listo');

    // ============================================
    // SECCIÓN 1: MANIPULACIÓN DEL DOM
    // ============================================

    initDOMManipulation();

    // ============================================
    // SECCIÓN 2: EVENTOS EN JQUERY
    // ============================================

    initToggleListEvent();

    // ============================================
    // SECCIÓN 3: PLUGIN DE BOOTSTRAP - TOOLTIPS
    // ============================================

    initBootstrapTooltips();
});

// ============================================
// FUNCIÓN 1: Manipulación del DOM
// ============================================
function initDOMManipulation() {
    console.log('→ Inicializando manipulación del DOM');

    // Cambiar el color de texto de los elementos de la lista
    $('#miLista li').css({
        'color': '#dc3545',        // Rojo
        'font-weight': 'bold',     // Texto grueso
        'font-size': '18px'        // Tamaño de fuente
    });
    console.log('  ✓ Colores de lista aplicados');

    // Evento: Cuando hacemos clic en el botón "Agregar Elemento 4"
    $('#agregarElemento').click(function() {
        // Añadir un nuevo <li> dinámicamente
        $('#miLista').append(
            '<li class="list-group-item" style="color: #28a745; font-weight: bold;">Elemento 4 (Añadido dinámicamente)</li>'
        );

        // Cambiar texto del botón
        $(this).text('¡Elemento añadido!');

        // Desactivar el botón (no se puede hacer clic más)
        $(this).attr('disabled', 'disabled');

        console.log('  ✓ Elemento 4 añadido a la lista');
    });
}

// ============================================
// FUNCIÓN 2: Eventos - Toggle Show/Hide
// ============================================
function initToggleListEvent() {
    console.log('→ Inicializando eventos de toggle');

    // Variable para rastrear si la lista está visible o oculta
    let listaVisible = true;

    // Evento: Cuando hacemos clic en el botón "toggleLista"
    $('#toggleLista').click(function() {
        // Si la lista está visible, ocultarla
        if (listaVisible) {
            // Ocultar la lista
            $('#listaToggle').hide();

            // Cambiar texto del botón
            $(this).text('Mostrar Lista');

            // Cambiar colores: quitar azul, añadir gris
            $(this).removeClass('btn-primary').addClass('btn-secondary');

            // Actualizar estado
            listaVisible = false;
            console.log('  ✓ Lista ocultada');
        }
        // Si la lista está oculta, mostrarla
        else {
            // Mostrar la lista
            $('#listaToggle').show();

            // Cambiar texto del botón
            $(this).text('Ocultar Lista');

            // Cambiar colores: quitar gris, añadir azul
            $(this).removeClass('btn-secondary').addClass('btn-primary');

            // Actualizar estado
            listaVisible = true;
            console.log('  ✓ Lista mostrada');
        }
    });
}

// ============================================
// FUNCIÓN 3: Plugin Bootstrap - Tooltips
// ============================================
function initBootstrapTooltips() {
    console.log('→ Inicializando tooltips de Bootstrap');

    // Buscar todos los elementos con data-bs-toggle="tooltip"
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));

    // Para cada elemento encontrado, crear un nuevo tooltip
    const tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    console.log('  ✓ Tooltips inicializados: ' + tooltipTriggerList.length);
}
