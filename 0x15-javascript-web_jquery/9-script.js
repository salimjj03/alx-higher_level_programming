$('document').ready(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  $.get(url, (data, textStatus) => {
    $('DIV#hello').text(data.hello);
  });
});
