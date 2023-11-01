$.get('https://swapi.co/api/films/?format=json', function (data) {
  // Loop through the movies and add their titles to the list
  $('UL#list_movies').append(...data.results.map(movie => `<li>${movie.title}</li>`));
});
