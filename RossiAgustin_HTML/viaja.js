
    const contactoForm = document.getElementById('contactoForm');
    
    contactoForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const nombre = contactoForm.querySelector('input[name="nombre"]').value;
        const email = contactoForm.querySelector('input[name="email"]').value;
        const mensaje = contactoForm.querySelector('textarea[name="mensaje"]').value;
        
        alert(`¡Mensaje enviado con éxito!\n\nGracias por contactarnos, ${nombre}.\nHemos recibido tu mensaje:\n\n${mensaje}\n\nTe responderemos pronto al email: ${email}`);
        
        contactoForm.reset();
    });

    const reservaForm = document.getElementById('reservaForm');
    const cantidadPasajes = reservaForm.querySelector('.numero');
    const botonMenos = reservaForm.querySelector('.menos');
    const botonMas = reservaForm.querySelector('.mas');
    const totalElement = document.getElementById('total');
    const precioPorPasaje = 1500;
    let cantidad = 1;

    botonMas.addEventListener('click', function() {
        cantidad++;
        cantidadPasajes.textContent = cantidad;
        actualizarTotal();
    });

    botonMenos.addEventListener('click', function() {
        if (cantidad > 1) {
            cantidad--;
            cantidadPasajes.textContent = cantidad;
            actualizarTotal();
        }
    });

    function actualizarTotal() {
        const total = cantidad * precioPorPasaje;
        totalElement.textContent = total;
    }

    reservaForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const destino = reservaForm.querySelector('select[name="destino"]').value;
        const fecha = reservaForm.querySelector('input[name="fecha"]').value;
        const hora = reservaForm.querySelector('select[name="hora"]').value;
        const nombre = reservaForm.querySelector('input[name="nombre"]').value;
        const email = reservaForm.querySelector('input[name="email"]').value;
        const telefono = reservaForm.querySelector('input[name="telefono"]').value;
        const total = cantidad * precioPorPasaje;
        
        alert(`¡Reserva realizada con éxito!\n\nDetalles de la reserva:\n\nDestino: ${destino.charAt(0).toUpperCase() + destino.slice(1)}\nCantidad de pasajes: ${cantidad}\nFecha: ${fecha}\nHorario: ${hora}hs\nCliente: ${nombre}\nEmail: ${email}\nTeléfono: ${telefono}\nTotal: $${total} USD`);
        
        reservaForm.reset();
        cantidad = 1;
        cantidadPasajes.textContent = '1';
        actualizarTotal();
    });

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
