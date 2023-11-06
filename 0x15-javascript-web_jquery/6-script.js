/*
 * Update the text for the header element
 * when the user clicks on the div whose
 * ID is update_header
 */
const header = $('header');

$('DIV#update_header').on('click', () => {
  header.text('New Header!!!');
});
