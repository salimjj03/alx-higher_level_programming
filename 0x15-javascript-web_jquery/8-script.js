const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, (data, textStatus) => {
  data.results.forEach((i) => {
    $('UL#list_movies').append('<li>' + i.title + '</li>');
  });
});
