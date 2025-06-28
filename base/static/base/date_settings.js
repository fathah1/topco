function saveDateFormat() {
  var dateFormatSelector = document.getElementById('dateFormat');
  const selectedFormat = dateFormatSelector.value;
  
  dateFormatter.setDateFormat(selectedFormat);
  saveDateFormatToBackend(selectedFormat);

}

function saveDateFormatToBackend(selectedFormat) {
  $.ajax({
      url: '/settings/save-date/',
      method: 'POST',
      data: { selected_format: selectedFormat, csrfmiddlewaretoken:getCookie('csrftoken') },
      success: function(response) {
        window.location.reload();
      },
      error: function (xhr, textStatus, errorThrown) {
        // Handle the error here
        console.error('Error:', errorThrown);
        window.location.reload();
      },
  });
}
