document.addEventListener('DOMContentLoaded', function() {
    const productos = document.querySelectorAll('.producto-item');
    const totalElement = document.getElementById('total');
    const btnConfirmar = document.getElementById('btnConfirmar');
    const aviso = document.getElementById('aviso');
    const confirmacion = document.getElementById('confirmacion');
    const ordenarSelect = document.getElementById('ordenar');
    let total = 0;

    // Funcionalidad de cantidades
    productos.forEach(producto => {
        const precio = parseInt(producto.getAttribute('data-precio'));
        const botonMenos = producto.querySelector('.btn-menos');
        const botonMas = producto.querySelector('.btn-mas');
        const numero = producto.querySelector('.cant-numero');
        const subtotal = producto.querySelector('.prod-subtotal');
        let cantidad = 0;

        botonMas.addEventListener('click', function() {
            cantidad++;
            numero.textContent = cantidad;
            const subtotalValor = cantidad * precio;
            subtotal.textContent = '$' + subtotalValor.toLocaleString();
            actualizarTotal();
        });

        botonMenos.addEventListener('click', function() {
            if (cantidad > 0) {
                cantidad--;
                numero.textContent = cantidad;
                const subtotalValor = cantidad * precio;
                subtotal.textContent = '$' + subtotalValor.toLocaleString();
                actualizarTotal();
            }
        });

        function actualizarTotal() {
            total = 0;
            productos.forEach(prod => {
                const prodPrecio = parseInt(prod.getAttribute('data-precio'));
                const prodCantidad = parseInt(prod.querySelector('.cant-numero').textContent);
                total += prodPrecio * prodCantidad;
            });
            totalElement.textContent = total.toLocaleString();
            
            if (total > 0) {
                btnConfirmar.disabled = false;
                aviso.style.display = 'none';
            } else {
                btnConfirmar.disabled = true;
                aviso.style.display = 'block';
            }
        }
    });

    // Funcionalidad de ordenar productos
    ordenarSelect.addEventListener('change', function() {
        const valor = this.value;
        const productosArray = Array.from(productos);
        const container = document.querySelector('.productos-lista');

        productosArray.sort((a, b) => {
            switch(valor) {
                case 'precio-asc':
                    return parseInt(a.getAttribute('data-precio')) - parseInt(b.getAttribute('data-precio'));
                case 'precio-desc':
                    return parseInt(b.getAttribute('data-precio')) - parseInt(a.getAttribute('data-precio'));
                case 'nombre':
                    const nombreA = a.querySelector('.prod-info h3').textContent.toLowerCase();
                    const nombreB = b.querySelector('.prod-info h3').textContent.toLowerCase();
                    return nombreA.localeCompare(nombreB);
                default:
                    return 0;
            }
        });

        productosArray.forEach(prod => container.appendChild(prod));
    });

    // Confirmar compra
    btnConfirmar.addEventListener('click', function() {
        const nombre = document.querySelector('input[name="name"]').value;
        const email = document.querySelector('input[name="email"]').value;
        const telefono = document.querySelector('input[name="phone"]').value;
        const direccion = document.querySelector('input[name="direccion"]').value;

        if (!nombre || !email || !telefono || !direccion) {
            alert('Por favor, completa todos tus datos.');
            return;
        }

        confirmacion.style.display = 'block';
        btnConfirmar.disabled = true;
        
        // Resetear formulario después de 3 segundos
        setTimeout(() => {
            productos.forEach(prod => {
                prod.querySelector('.cant-numero').textContent = '0';
                prod.querySelector('.prod-subtotal').textContent = '$0';
            });
            total = 0;
            totalElement.textContent = '0';
            document.querySelectorAll('input').forEach(input => input.value = '');
            btnConfirmar.disabled = true;
            aviso.style.display = 'block';
            confirmacion.style.display = 'none';
        }, 3000);
    });

    // Smooth scroll en navegación
    const navLinks = document.querySelectorAll('nav a');
    
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if (targetId.startsWith('#')) {
                e.preventDefault();
                const targetSection = document.querySelector(targetId);
                if (targetSection) {
                    targetSection.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });
});
