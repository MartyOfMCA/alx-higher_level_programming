/*
 * Fetch a character name use the Star Was
 * API displaying the fetched value in
 * an element.
 */
const character = $('DIV#character');

$(document).ready(() => {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', (data) => {
    character.text(data.name);
  });
});
