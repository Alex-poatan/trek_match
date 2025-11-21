// main.js - comportamiento mínimo para demo de e-commerce (localStorage simple)
$(document).ready(function(){
  // Añadir al carro desde botones
  $('.add-to-cart').on('click', function(){
    const id = $(this).data('id');
    const name = $(this).data('name');
    const price = Number($(this).data('price'));
    addToCart({id,name,price,qty:1});
    alert('Añadido al carro: '+name);
  });

  // Si estamos en product.html, cargar datos simulados según id query
  // Nota: la lógica de product detail está embedded en product.html (catalogo centrado en Torres del Paine)

  // Si estamos en cart.html, mostrar items
  if(window.location.pathname.endsWith('cart.html')){
    renderCart();
    $('#checkout').on('click', function(){ alert('Simulación: checkout iniciado.'); localStorage.removeItem('trek_cart'); renderCart(); });
  }

  function addToCart(item){
    const raw = localStorage.getItem('trek_cart');
    const cart = raw? JSON.parse(raw):[];
    const found = cart.find(x=>x.id==item.id);
    if(found){ found.qty += item.qty; } else { cart.push(item); }
    localStorage.setItem('trek_cart', JSON.stringify(cart));
  }

  function renderCart(){
    const raw = localStorage.getItem('trek_cart');
    const cart = raw? JSON.parse(raw):[];
    const $c = $('#cart-contents');
    $c.empty();
    if(cart.length===0){ $c.html('<p>Tu carro está vacío.</p>'); return; }
    let total=0;
    const $table = $('<table class="table" />');
    $table.append('<thead><tr><th>Producto</th><th>Cantidad</th><th>Precio</th></tr></thead>');
    const $body = $('<tbody/>');
    cart.forEach(i=>{ total += i.price * i.qty; $body.append('<tr><td>'+i.name+'</td><td>'+i.qty+'</td><td>CLP $'+(i.price*1000* i.qty)+'</td></tr>'); });
    $table.append($body);
    $c.append($table);
    $c.append('<p class="fw-bold">Total estimado: CLP $'+(total*1000)+' (precio mostrado en miles)</p>');
  }

});
