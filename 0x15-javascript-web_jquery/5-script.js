/*
 * Add a list item to a list when the user
 * clicks on a div with the ID of
 * add_item.
 */
const list = $('UL.my_list');

$('DIV#add_item').on('click', () => {
  list.append('<li>Item</li>');
});
