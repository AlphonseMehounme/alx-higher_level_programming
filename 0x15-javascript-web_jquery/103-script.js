document.addEventListener('DOMContentLoaded', function () {
  $('INPUT#btn_translate').on('click', function () { 
    var lang = $('INPUT#language_code').val();
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + lang, function (data, status) {
      $('DIV#hello').append(data.hello);
    });
  });
  $('INPUT#language_code').on('keydown', function (event) {
    if (event.key === 'Enter') {
      var lang = $('INPUT#language_code').val();
      $.get('https://hellosalut.stefanbohacek.dev/?lang=' + lang, function (data, status) {
        $('DIV#hello').append(data.hello);
      });
    }
  });
});
