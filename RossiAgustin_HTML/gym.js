document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('reservaForm');
    
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const clase = form.querySelector('select[name="clase"]').value;
        const nombre = form.querySelector('input[name="name"]').value;
        const telefono = form.querySelector('input[name="phone"]').value;
        const dia = form.querySelector('select[name="day"]').value;
        const horario = form.querySelector('select[name="time"]').value;
        const entrenador = form.querySelector('select[name="entrenador"]').value;
        const nota = form.querySelector('textarea[name="note"]').value;
        
        if (!clase) {
            alert('Por favor, selecciona una clase.');
            return;
        }
        
        if (!dia) {
            alert('Por favor, selecciona un día.');
            return;
        }
        
        if (!horario) {
            alert('Por favor, selecciona un horario.');
            return;
        }
        
        if (!entrenador) {
            alert('Por favor, selecciona un entrenador.');
            return;
        }
        
        alert(`¡Reserva realizada con éxito!\n\nDetalles de la reserva:\n\nCliente: ${nombre}\nTeléfono: ${telefono}\nClase: ${clase.charAt(0).toUpperCase() + clase.slice(1)}\nDía: ${dia}\nHorario: ${horario}hs\nEntrenador: ${entrenador}\nNota: ${nota || 'Sin nota'}`);
        
        form.reset();
    });
});