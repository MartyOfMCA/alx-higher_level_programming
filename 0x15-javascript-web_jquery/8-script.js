/*
 * Fetch the title for all movies using the Star
 * Wars API. The fetched data is displayed in
 * a list.
 */
const list = $('UL#list_movies');

$(document).ready(() => {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data) => {
    $(data.results).each((index, film) => {
      list.append(`<li>${film.title}</li>`);
    });
  });
});
