$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, status) {
  const movies = data.results;
  $.each(movies, function (i, movie) {
    $('UL#list_movies').append('<li>' + movie.title + '</li>');
  });
});
