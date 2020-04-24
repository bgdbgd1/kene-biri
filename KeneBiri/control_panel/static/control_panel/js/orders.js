function deleteDriver(driverId) {
    $.ajax({
      dataType: 'json',
      url: '',
      method: 'delete',
      data,
      contentType: options.contentType,
      success: (response) => {
          location.reload();
      }
    });
}