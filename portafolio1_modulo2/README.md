# TrekMatch.cl — Portafolio / Demo Frontend

Proyecto de ejemplo para el portafolio del alumno: frontend de una tienda de e‑commerce / marketplace de experiencias de trekking.

Resumen:
- Nombre comercial: TrekMatch.cl
- Tagline: "El trekking que realmente quieres, con el guía perfecto para ti."
- Modelo: marketplace + e‑commerce de experiencias (paquetes de trekking como producto).

Qué contiene esta carpeta (`portafolio1_modulo2`):

- `index.html` — página principal con barra de navegación, listado de experiencias en tarjetas, botones para comprar y enlace al carro.
- `product.html` — página de detalle de producto (demo) que se consulta por query string `?id=1`.
- `cart.html` — carro simple que muestra los artículos añadidos (usa `localStorage`).
- `assets/css/styles.css` — estilos personalizados mínimos.
- `assets/js/main.js` — lógica mínima con jQuery para añadir al carro, renderizar carro y simular checkout.

Tecnologías empleadas:
- HTML5
- CSS3 (Bootstrap 5 por CDN)
- JavaScript + jQuery (por CDN)

Descripción del proyecto (para README del repositorio):

TrekMatch.cl es una plataforma que vende experiencias de trekking. En esta versión de demostración el contenido está centrado en las experiencias de <strong>Torres del Paine</strong>, en particular el <em>Circuito W</em> y el <em>Circuito O</em>. Cada experiencia es un producto que incluye fecha, ruta, dificultad, cupo y precio. El rasgo diferencial propuesto es un sistema de "matching" que asigna automáticamente el guía ideal según el perfil del cliente (nivel físico, tipo de experiencia, tamaño del grupo, preferencias, presupuesto).

Este repositorio contiene el Frontend demo (estático) que muestra cómo presentar los productos (Circuito W y O), navegar a la página de detalle y gestionar un carro de compras básico.

Cómo probar localmente:
1. Abrir `index.html` en el navegador (doble clic o servidor local).
2. Hacer click en "Comprar" para añadir al carro.
3. Ir a `cart.html` para ver los artículos añadidos.

Notas para el profesor / revisor:
- Es un prototipo frontend, pensado para evaluación del diseño y estructura. El backend y el sistema real de matching no están implementados en este repositorio — sólo se demuestra la interfaz y el flujo de compra mínimo.

Autor: Alexander
