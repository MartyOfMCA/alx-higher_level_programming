/*
 * Fetch the greeting for the given language
 * using an API.
 * The user would provide the language that
 * matches any of the valid languages. Then
 * a call is made to retrieve the greeting
 * using the API. The default language would
 * always be English (even when the user
 * provides and invalid language.
 */
const fetchGreeting = () => {
  let found = false;
  let language = 'en';
  const input = $('INPUT#language_code')['0'].value;

  language = input !== '' ? input : 'de';

  const languages = ['ar', 'az', 'be', 'bg', 'bn', 'bs',
    'cs', 'da', 'de', 'dz', 'el', 'en', 'en-gb',
    'en-us', 'es', 'et', 'fa', 'fi', 'fil', 'fr',
    'he', 'hi', 'hr', 'hu', 'hy', 'id', 'is', 'it',
    'ja', 'ka', 'kk', 'km', 'ko', 'lb', 'lo', 'lt',
    'lv', 'mk', 'mn', 'ms', 'my', 'ne', 'no', 'pl',
    'pt', 'ro', 'ru', 'sk', 'sl', 'sq', 'sr', 'sv',
    'sw', 'th', 'tk', 'uk', 'vi', 'zh'];

  $.each(languages, (index, value) => {
    if (language === value) {
      found = true;
    }
  });

  language = found ? language : 'en';

  $.get(`https://hellosalut.stefanbohacek.dev/?lang=${language}`, (data) => {
    $('DIV#hello').text(data.hello);
  });
};

$(document).ready(() => {
  $('INPUT#btn_translate').on('click', fetchGreeting);
  $('INPUT#language_code').focus(() => {
    $('INPUT#language_code').keypress((event) => {
      if (event.originalEvent.key === 'Enter') {
        fetchGreeting();
      }
    });
  });
});
