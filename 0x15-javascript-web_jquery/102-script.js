document.addEventListener('DOMContentLoaded', function () {
  $('INPUT#btn_translate').on('click', function () {
    const lang = $('INPUT#language_code').val();
    console.log(lang);
    $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data, status) {
      $('DIV#hello').append(data.hello);
    });
  });
});
