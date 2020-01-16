// Carrito - Tick en tarjeta producto

function changeProductCardOverview(element) {
    if (element.hasAttribute('added')) {
        element.removeAttribute('added');
        element.innerHTML = '<i class="fas fa-cart-plus"></i>';

    } else {
        element.setAttribute('added', 'true');
        element.innerHTML = '<i class="fas fa-check-circle" style="color:green;"></i>';
    }
}