/*
 * Change the header element color to red
 * when the user clicks the div element with
 * the ID red_header
 */

$('DIV#red_header').on('click', () => {
  $('header').css('color', '#FF0000');
});
