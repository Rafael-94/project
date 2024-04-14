$(document).ready(function () {
  $('.marcar-realizada').click(function () {
    var tareaId = $(this).data('tarea-id');
    var csrfToken = $('#csrf_token').val(); // Obtener el token CSRF desde el input hidden

    // Realizar la solicitud AJAX para eliminar la tarea
    $.ajax({
      url: `/tareas/${tareaId}/borrar/`,
      type: 'POST',
      headers: {
        'X-CSRFToken': csrfToken // Incluir el token CSRF en los encabezados
      },
      success: function (data) {
        console.log('La tarea se ha eliminado correctamente.');
        // Puedes realizar alguna acción adicional si lo deseas, como recargar la página
        location.reload();
      },
      error: function (xhr, errmsg, err) {
        console.error('Error al eliminar la tarea:', errmsg);
        // Puedes manejar errores si es necesario
      }
    });
  });
});
