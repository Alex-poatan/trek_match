# Servicios Profesionales — Portafolio / Demo Frontend

Carpeta de demo para un portafolio orientado a servicios de consultoría en transformación digital, analítica y optimización operacional.

Resumen de la oferta (presentada en la demo):
- Analítica de Datos para Decisiones de Negocio: dashboards ejecutivos, forecasting, optimización de inventarios, automatización de reportería.
- Mejora de Procesos y Reducción de Costos: Lean, Six Sigma, VSM, simulación de procesos y diseño de KPIs.
- Dirección y Evaluación de Proyectos: gestión PMI, evaluación económica (TIR/VAN), control de riesgos y cronogramas.
- E-Commerce y Transformación Digital: implementación de tiendas online, integración de pagos y automatización comercial.
- Estrategia de Sostenibilidad y Cumplimiento Ambiental: cálculo de huella de carbono (ISO 14064-1), estrategias ESG y Ley REP.

Qué contiene esta carpeta (`portafolio1_modulo2`):

- `index.html` — página principal con navegación y tarjetas de servicios.
- `product.html` — página de detalle por servicio (`?id=1..5`).
- `cart.html` — carrito/solicitudes simple que usa `localStorage` para simular solicitudes de contacto.
- `assets/css/styles.css` — estilos.
- `assets/js/main.js` — lógica para añadir servicios al carro y representar el contenido.

Tecnologías empleadas:
- HTML5
- CSS3 (Bootstrap 5 por CDN)
- JavaScript + jQuery (por CDN)

Cómo probar localmente:
1. Abrir `index.html` en el navegador (doble clic) o ejecutar un servidor local (recomendado).
	- Con Live Server (VS Code) o con Python: `python -m http.server 5500` y abrir `http://localhost:5500`.
2. Usar la caja de búsqueda para filtrar servicios y la barra lateral para seleccionar categorías.
3. Pulsar "Contactar" en una tarjeta para abrir el modal de cotización (se guarda una solicitud simulada en `localStorage`).
4. Ver las solicitudes en `cart.html`.

Cambios principales en esta versión:
- Nuevo tema oscuro y estilo moderno acorde a un portafolio B2B.
- Búsqueda en vivo y filtrado por categorías.
- Tarjetas con overlay, efectos de hover y CTA de contacto.
- Modal de cotización para capturar datos básicos del cliente.
- Carro/solicitudes usando `localStorage` para simular flujo de e-commerce de servicios.

Notas:
- Esta carpeta es una demo front-end para mostrar la oferta de servicios de forma sencilla. No incluye backend ni integración real de pagos o CRM.

Autor: Alexander
