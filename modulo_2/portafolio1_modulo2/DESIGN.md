# Guía de diseño — Portafolio Servicios Profesionales

Esta guía resume la paleta de colores, gradientes y usos recomendados para la interfaz del portafolio.

## Paleta principal
- Primary Blue (brand-1): `#12A4FF` — color principal para identidad y acentos.
- Light Blue (brand-2): `#6BE1FF` — segundo color para gradientes y botones.
- Accent (purple): `#7B5CFF` — color de apoyo para elementos destacados.
- Fondo (bg): `#0B1218` — fondo oscuro neutro.
- Superficie (surface): `#0F1B24` — tarjetas y secciones.
- Texto secundario (muted): `#9AA6B2` — texto descriptivo y meta-información.

## Variables CSS definidas
En `assets/css/styles.css` se usan variables CSS como:
```
--brand-1, --brand-2, --accent, --bg, --surface, --muted
--cta-gradient: linear-gradient(90deg,var(--brand-1),var(--brand-2))
```
Usa `--cta-gradient` para botones principales (`.btn-cta`, `.btn-primary` en tarjetas).

## Botones
- Botón principal (CTA): fondo con `--cta-gradient`, texto oscuro, borde redondeado y sombra ligera.
- Botón secundario/outline: `border-color: rgba(255,255,255,0.45)` y hover con fondo semitransparente.

## Tarjetas de servicio
- Imagen en `background-image` con `cover` y una capa de overlay (degradado) para asegurar legibilidad del título.
- Título en blanco con `text-shadow` para mejor contraste sobre imágenes.
- CTA: dos botones en la parte inferior (Ver detalle / Contactar). El segundo usa el `--cta-gradient`.

## Tipografía
- `Inter` (Google Fonts) en pesos 300/400/600/700.
- Tamaños: los títulos de tarjeta son ligeramente mayores en móvil para emular el pantallazo.

## Recomendaciones UX
- Para servicios, evita mostrar precios fijos sin contexto; mostrar `A consultar` o rango inicial y usar CTA "Cotizar".
- Considera renombrar "Carro" a "Solicitudes" o "Presupuesto" si el flujo es de solicitud de cotización en lugar de venta directa.

## Iconografía e imágenes
- Las imágenes en el grid deben ser reales (casos/portafolio) y estar recortadas al mismo formato. Usa un overlay oscuro para consistencia.

## Accesibilidad
- Asegurar contraste suficiente en texto importante (WCAG AA). Para CTAs con gradiente, se recomienda añadir borde o sombra para mejorar legibilidad.

---

Si quieres, genero un pequeño archivo `palette.png` con la paleta y ejemplos de botones para usar en presentaciones o mockups.
