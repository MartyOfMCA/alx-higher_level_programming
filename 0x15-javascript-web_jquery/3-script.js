/*
 * Add a new class to the header element
 * when the user clicks the div element with
 * the ID red_header
 */

$('DIV#red_header').on('click', () => {
  $('header').addClass('red');
});
