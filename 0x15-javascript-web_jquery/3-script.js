$(document).ready(function () {
  const redHeaderDiv = $('DIV#red_header');

  redHeaderDiv.click(function () {
    const headerElement = $('header');

    if (headerElement) {
      headerElement.addClass('red');
    } else {
      console.error('Header elemnet not found');
    }
  });
});
