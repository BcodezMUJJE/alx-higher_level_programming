$.get('https://swapi.co/api/people/5/?format=json', function (data) {
  // Display the character name in the HTML tag
  $('DIV#character').text(data.name);
});
