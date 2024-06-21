document.addEventListener('DOMContentLoaded', function () {
  $('INPUT#btn_translate').on('click', function () {
    const lang = $('INPUT#language_code').val();
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + lang, function (data, status) {
      $('DIV#hello').append(data.hello);
    });
  });
});
