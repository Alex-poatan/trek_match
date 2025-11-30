// main.js - comportamiento mínimo para demo de servicios (localStorage simple)
$(document).ready(function(){
  // Añadir al carro/solicitudes desde botones que tengan la clase .add-to-cart
  $('.add-to-cart').on('click', function(){
    const id = $(this).data('id');
    const name = $(this).data('name');
    const price = Number($(this).data('price')) || 0;
    addToCart({id,name,price,qty:1});
    alert('Solicitud añadida: '+name);
  });

  // Si estamos en cart.html, mostrar items
  if(window.location.pathname.endsWith('cart.html')){
    renderCart();
    $('#checkout').on('click', function(){ alert('Simulación: solicitud enviada.'); localStorage.removeItem('service_cart'); renderCart(); });
  }

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
    const $table = $('<table class="table" />');
    $table.append('<thead><tr><th>Servicio</th><th>Cantidad</th><th>Precio</th></tr></thead>');
    const $body = $('<tbody/>');
    cart.forEach(i=>{ total += i.price * i.qty; const displayPrice = i.price? ('CLP $'+(i.price*1000*i.qty)) : 'A consultar'; $body.append('<tr><td>'+i.name+'</td><td>'+i.qty+'</td><td>'+displayPrice+'</td></tr>'); });
    $table.append($body);
    $c.append($table);
    $c.append('<p class="fw-bold">Total estimado: CLP $'+(total*1000)+' (si aplica). Para servicios consulte condiciones.</p>');
  }

});
