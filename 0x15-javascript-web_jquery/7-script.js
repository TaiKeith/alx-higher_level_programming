$.ajax({
    url: 'https://swap-api.alx-tools.com/api/people/5/?format=json',
    method: 'GET',
    datatype: 'json',
    success: function (data) {
        const characterName = data.name;

	$('DIV#character').text(characterName);
    }
});
