/*
 * Fetch value from an API and update element
 * with fetched value after page finishes
 * loading.
 */
$(document).ready(() => {
  const container = $('DIV#hello');
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (data) => {
    container.text(data.hello);
  });
});
