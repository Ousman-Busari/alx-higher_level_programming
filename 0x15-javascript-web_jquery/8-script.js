$.get(
  "https://swapi-api.alx-tools.com/api/films/?format=json",
  function (data, textStatus) {
    const results = data.results
    $.each(results, function (index, item) {
      $("#list_movies").append("<li>" + item.title + "</li>");
    });
  }
);
