//
//

const startStopBtn = document.getElementById("btn");
const dateTimeElement = document.getElementById("datetime");

var intervalId = 0;

function showTest() {
  var dateTime = new Date();
  options = {
    hour: "numeric",
    minute: "numeric",
    second: "numeric",
  };
  dateTime = dateTime.toLocaleDateString("ru-RU", options);
  dateTimeElement.innerHTML = `<p>${dateTime}</p>`;
}

function intervalManager() {
  if (intervalId === 0) {
    intervalId = setInterval(showTest, 1000);
    startStopBtn.textContent = "Stop";
  } else {
    clearInterval(intervalId);
    intervalId = 0;
    startStopBtn.textContent = "Start";
  }
}

showTest();
startStopBtn.addEventListener("click", intervalManager);
