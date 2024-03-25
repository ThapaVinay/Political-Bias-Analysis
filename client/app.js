function onClickedBias() {
  var text = document.getElementById("uiText");
  var bias = document.getElementById("uiBias");

  var url = "http://127.0.0.1:5000/predict_bias";

  $.post(
    url,
    {
      text: text,
    },
    function (data, status) {
      bias.innerHTML = "<h2>" + data.bias.toString() + "</h2>";
      console.log(status);
    }
  );
}
