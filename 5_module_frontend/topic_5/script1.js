function sayHello(event) {
  usernameElement = document.getElementById("username");
  console.log("Мы получили ваш юзернейм:", usernameElement.value);
  alert("Hello in console " + usernameElement.value + "!");
}

function handleSubmit(event) {
  usernameElement = document.getElementById("username");
  resultElement = document.getElementById("result");

  resultElement.innerHTML = `Hello ${usernameElement.value}`;
  alert("stop");
}

addEventListener("submit", handleSubmit);
