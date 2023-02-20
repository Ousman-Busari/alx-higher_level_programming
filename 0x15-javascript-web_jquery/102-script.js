$("document").ready(function () {
  $("#language_code").focus();
  let url = "https://www.fourtonfish.com/hellosalut/hello/";
  $("#btn_translate").click(function () {
    const lang_code = $("#language_code").val();
    url += "?lang=" + lang_code;
    $.get(url, function (data) {
      $("#hello").text(data.hello);
    });
  });
});
