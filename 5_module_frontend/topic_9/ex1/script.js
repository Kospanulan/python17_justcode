//
//

const startStopBtn = document.getElementById("btn");
const logElement = document.getElementById("log");

var intervalId = 0;

function showTest() {
  //   console.log("Test");
  pElement = document.createElement("p");
  pElement.textContent = "test";
  logElement.appendChild(pElement);
}

function intervalManager() {
  if (intervalId === 0) {
    intervalId = setInterval(showTest, 2000);
    startStopBtn.textContent = "Stop";
  } else {
    clearInterval(intervalId);
    intervalId = 0;
    startStopBtn.textContent = "Start";
  }
}

startStopBtn.addEventListener("click", intervalManager);
