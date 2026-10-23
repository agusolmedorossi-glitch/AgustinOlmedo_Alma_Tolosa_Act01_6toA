const productos = document.querySelectorAll(".producto");
const totalSpan = document.getElementById("total");
const btnConfirmar = document.getElementById("btnConfirmar");
const aviso = document.getElementById("aviso");
const confirmacion = document.getElementById("confirmacion");
const pedidoForm = document.getElementById("pedidoForm");
const btnAceptar = document.querySelector(".btn-aceptar");
const btnRechazar = document.querySelector(".btn-rechazar");

function actualizarTotal() {
  let total = 0;
  let cantidadTotal = 0;

  productos.forEach(function (producto) {
    const precio = Number(producto.dataset.precio);
    const cantidad = Number(producto.querySelector(".numero").textContent);
    const subtotal = precio * cantidad;

    producto.querySelector(".subtotal").textContent = "$" + subtotal.toLocaleString("es-AR");
    total += subtotal;
    cantidadTotal += cantidad;
  });

  totalSpan.textContent = total.toLocaleString("es-AR");

  // Habilitar/deshabilitar botón según si hay productos
  btnConfirmar.disabled = cantidadTotal === 0;

  // Mostrar/ocultar aviso
  aviso.style.display = cantidadTotal === 0 ? "block" : "none";
}

productos.forEach(function (producto) {
  const numero = producto.querySelector(".numero");

  producto.querySelector(".mas").addEventListener("click", function () {
    numero.textContent = Number(numero.textContent) + 1;
    actualizarTotal();
  });

  producto.querySelector(".menos").addEventListener("click", function () {
    const actual = Number(numero.textContent);
    if (actual > 0) {
      numero.textContent = actual - 1;
      actualizarTotal();
    }
  });
});

pedidoForm.addEventListener("submit", function (event) {
  event.preventDefault();

  const total = Number(totalSpan.textContent.replace(/\./g, "").replace(/,/g, ""));

  if (total === 0) {
    return;
  }

  const formData = new FormData(pedidoForm);

  const order = {
    customer: {
      name: formData.get("name"),
      phone: formData.get("phone"),
    },
    pickup: {
      day: formData.get("day"),
      time: formData.get("time"),
    },
    note: formData.get("note"),
    products: [],
    total: total,
  };

  // Recopilar productos seleccionados
  productos.forEach(function (producto) {
    const nombre = producto.querySelector("h3").textContent;
    const precio = Number(producto.dataset.precio);
    const cantidad = Number(producto.querySelector(".numero").textContent);

    if (cantidad > 0) {
      order.products.push({
        name: nombre,
        quantity: cantidad,
        unitPrice: precio,
      });
    }
  });

  console.log("Pedido generado:", order);

  // Mostrar confirmación
  confirmacion.style.display = "block";

  // Ocultar confirmación después de 5 segundos
  setTimeout(function () {
    confirmacion.style.display = "none";
  }, 5000);
});

// Botones de términos y condiciones
btnAceptar.addEventListener("click", function () {
  alert("¡Gracias por aceptar nuestros términos y condiciones! Puedes continuar con tu pedido.");
});

btnRechazar.addEventListener("click", function () {
  alert("Debes aceptar los términos y condiciones para realizar un pedido.");
});

// Inicializar estado
actualizarTotal();
