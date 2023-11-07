/*
 * Add, remove and clear list items from a list
 * when the user interacts with the appropciate
 * buttons.
 */
$(document).ready(() => {
  const list = $('UL.my_list');

  $('DIV#add_item').on('click', () => {
    list.append('<li>Item</li>');
  });
  $('DIV#remove_item').on('click', () => {
    $('UL.my_list>LI:last-child').remove();
  });
  $('DIV#clear_list').on('click', () => {
    list.empty();
  });
});
