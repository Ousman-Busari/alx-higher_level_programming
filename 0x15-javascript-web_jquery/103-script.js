$("document").ready(function () {
  $("#btn_translate").click(translate);
  $("#language_code").focus();
  $("#language_code").focus(function () {
    $("#language_code").keypress((e) => {
      if (e.which === 13) {
        translate();
      }
    });
  });
});

function translate() {
  let url = "https://www.fourtonfish.com/hellosalut/hello/";
  const lang_code = $("#language_code").val();
  $.get(url + $.param( {lang: lang_code}), function (data) {
    $("#hello").text(data.hello);
  });
}
