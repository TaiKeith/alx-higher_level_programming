$.ajax({
  url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
  method: 'GET',
  dataType: 'json',
  success: function (data) {
    const translation = data.hello;

    $('DIV#hello').text(translation);
  }
});
