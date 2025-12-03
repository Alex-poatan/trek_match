// main.js - mejoras: renderizado dinámico, búsqueda, filtrado, modal de contacto y carrito simple
$(document).ready(function(){
  // Catálogo de servicios (puede ampliarse)
  const catalog = [
    {id:1,cat:'analitica',title:'Analítica de Datos para Decisiones de Negocio',desc:'Dashboards ejecutivos, forecasting, optimización de inventarios y automatización de reportería.',price:300,img:'assets/img/Analitica_de_datos/1.png'},
    {id:2,cat:'procesos',title:'Mejora de Procesos y Reducción de Costos',desc:'Diagnóstico y optimización operacional con Lean, Six Sigma y simulación.',price:350,img:'assets/img/Mejora_de_proceso/2.png'},
    {id:3,cat:'proyectos',title:'Dirección y Evaluación de Proyectos',desc:'Gestión integral bajo estándares PMI, planificación, control y evaluación económica.',price:280,img:'assets/img/Direccion_de_proyectos/3.png'},
    {id:4,cat:'ecommerce',title:'E-Commerce y Transformación Digital',desc:'Desarrollo de tiendas online, integración de pagos y automatización comercial.',price:400,img:'assets/img/E-commerce/4.png'},
    {id:5,cat:'sostenibilidad',title:'Estrategia de Sostenibilidad y Cumplimiento Ambiental',desc:'Economía circular, huella de carbono y reportes ESG.',price:320,img:'assets/img/Sostenibilidad/5.png'}
  ];

  // Render catalog on index
  function renderCatalog(list){
    const $root = $('#product-list');
    $root.empty();
    list.forEach(s => {
      const $col = $("<div class='col-6 col-md-4 col-xl-3'></div>");
      const $card = $("<article class='service-card p-0'></article>");
      const $thumb = $("<div class='thumb'></div>").css('background-image', `url(${s.img})`);
      const $overlay = $("<div class='overlay'></div>");
      $overlay.append(`<div class='service-badge'>${s.cat}</div>`);
      $overlay.append(`<h5>${s.title}</h5>`);
      $overlay.append(`<p class='d-none d-md-block'>${s.desc}</p>`);
      const $actions = $(`<div class='service-actions'></div>`);
      $actions.append(`<a href='product.html?id=${s.id}' class='btn btn-sm btn-outline-light'>Ver detalle</a>`);
      $actions.append(`<button class='btn btn-sm btn-primary ms-2 add-to-cart' data-id='${s.id}' data-name='${s.title}' data-price='${s.price}'>Contactar</button>`);
      $overlay.append($actions);
      $card.append($thumb).append($overlay);
      $col.append($card);
      $root.append($col);
    });
  }

  renderCatalog(catalog);

  // Search filter
  $('#search').on('input', function(){
    const q = $(this).val().trim().toLowerCase();
    const filtered = catalog.filter(s => s.title.toLowerCase().includes(q) || s.desc.toLowerCase().includes(q));
    renderCatalog(filtered);
  });

  // Category filter (delegated)
  $(document).on('click', '.category-item', function(e){
    e.preventDefault();
    const cat = $(this).data('cat');
    $('.category-item').removeClass('active');
    $(this).addClass('active');
    if(cat==='all') renderCatalog(catalog); else renderCatalog(catalog.filter(s=>s.cat===cat));
  });

  // Delegated add-to-cart from dynamically rendered cards
  $(document).on('click', '.add-to-cart', function(){
    const id = $(this).data('id');
    const name = $(this).data('name');
    const price = Number($(this).data('price')) || 0;
    addToCart({id,name,price,qty:1});
    // Open solicitud modal (shows current selection and form)
    renderSolicitudList();
    const modal = new bootstrap.Modal(document.getElementById('contactModal'));
    modal.show();
  });

  // Solicitud modal send button - envía la selección con datos del cliente
  $('#sol-send').on('click', function(){
    const name = $('#sol-name').val();
    const email = $('#sol-email').val();
    const msg = $('#sol-msg').val();
    const raw = localStorage.getItem('service_cart');
    const cart = raw? JSON.parse(raw):[];
    if(cart.length===0){ alert('No hay servicios seleccionados.'); return; }
    if(!name || !email || !msg){ alert('Por favor completa nombre, email y descripción.'); return; }
    // Crear objeto de solicitud
    const solicitud = {
      id: 'REQ-' + Date.now(),
      contact:{name,email},
      message: msg,
      items: cart,
      created: new Date().toISOString()
    };
    // Guardar en localStorage como historial de solicitudes (simulación de envío)
    const rawSent = localStorage.getItem('sent_requests');
    const sent = rawSent? JSON.parse(rawSent):[];
    sent.push(solicitud);
    localStorage.setItem('sent_requests', JSON.stringify(sent));
    // Vaciar carrito / selección
    localStorage.removeItem('service_cart');
    // Cerrar modal
    const modalEl = document.getElementById('contactModal');
    const modal = bootstrap.Modal.getInstance(modalEl);
    modal.hide();
    // Feedback
    alert('Solicitud enviada correctamente. Te contactaremos por email con una propuesta ajustada.');
    // limpiar formulario
    $('#solicitud-form')[0].reset();
  });

  // Render contents of solicitud modal (list selected services)
  function renderSolicitudList(){
    const raw = localStorage.getItem('service_cart');
    const cart = raw? JSON.parse(raw):[];
    const $list = $('#solicitud-list');
    $list.empty();
    if(cart.length===0){ $list.html('<p class="text-muted">No hay servicios seleccionados.</p>'); return; }
    cart.forEach(i => {
      $list.append(`<div class='mb-2'><strong>${i.name}</strong> <span class='text-muted'>x${i.qty}</span></div>`);
    });
  }

  // Cart page render
  if(window.location.pathname.endsWith('cart.html')){
    renderCart();
    // Abrir modal de solicitud desde la página de solicitudes
    $('#open-solicitud-modal').on('click', function(){
      renderSolicitudList();
      const modal = new bootstrap.Modal(document.getElementById('contactModal'));
      modal.show();
    });
  }

  // Cart helpers
  function addToCart(item){
    const raw = localStorage.getItem('service_cart');
    const cart = raw? JSON.parse(raw):[];
    const found = cart.find(x=>x.id==item.id);
    if(found){ found.qty += item.qty; } else { cart.push(item); }
    localStorage.setItem('service_cart', JSON.stringify(cart));
  }

  function renderCart(){
    const raw = localStorage.getItem('service_cart');
    const cart = raw? JSON.parse(raw):[];
    const $c = $('#cart-contents');
    $c.empty();
    if(cart.length===0){ $c.html('<p>Tu carro está vacío.</p>'); return; }
    let total=0;
    const $table = $('<table class="table table-dark table-striped" />');
    $table.append('<thead><tr><th>Servicio</th><th>Cantidad</th><th>Precio</th></tr></thead>');
    const $body = $('<tbody/>');
    cart.forEach(i=>{ total += (i.price||0) * i.qty; const displayPrice = i.price? ('CLP $'+(i.price*1000*i.qty)) : 'A consultar'; $body.append('<tr><td>'+i.name+'</td><td>'+i.qty+'</td><td>'+displayPrice+'</td></tr>'); });
    $table.append($body);
    $c.append($table);
    $c.append('<p class="fw-bold">Total estimado: CLP $'+(total*1000)+' (si aplica). Para servicios consulte condiciones.</p>');
  }

});
