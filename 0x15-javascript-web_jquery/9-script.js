$('document').ready(function () {
  // Display the translation of "hello" in the HTML tag
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    $('DIV#hello').text(data.hello);
  });
});
