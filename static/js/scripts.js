$(document).ready(function () {
  $('.guardar-tarea').click(function () {
    var botonGuardar = $(this); // Guardar referencia al botón "Guardar" que se hizo clic
    var tareaId = botonGuardar.data('tarea-id');
    var realizada = botonGuardar.closest('tr').find('.tarea-realizada-checkbox').prop('checked');
    var csrfToken = $('#csrf_token').val(); // Obtener el token CSRF desde el input hidden

    // Realizar la solicitud AJAX para marcar la tarea como realizada
    $.ajax({
      url: `/marcar_realizada/${tareaId}/`,
      type: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken // Incluir el token CSRF en los encabezados
      },
      data: JSON.stringify({ realizada: realizada }),
      success: function (data) {
        console.log('La tarea se marcó como realizada correctamente.');
        // Agregar la clase tarea-realizada a la fila correspondiente
        if (realizada) {
          botonGuardar.closest('tr').addClass('tarea-realizada');
        } else {
          botonGuardar.closest('tr').removeClass('tarea-realizada');
        }
      },
      error: function (xhr, errmsg, err) {
        console.error('Error al marcar la tarea como realizada:', errmsg);
        // Puedes manejar errores si es necesario
      }
    });
  });
});
