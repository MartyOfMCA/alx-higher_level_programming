/*
 * Manually toggle between the classes red
 * and green on the header element
 * when the user clicks the div element with
 * the ID toggle_header
 */
const header = $('header');

$('DIV#toggle_header').on('click', () => {
  if (header.hasClass('green')) {
    header.removeClass('green');
    header.addClass('red');
  } else {
    header.removeClass('red');
    header.addClass('green');
  }
});
