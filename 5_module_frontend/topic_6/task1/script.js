const btnElem = document.getElementById("btn");
const numberOneElem = document.getElementById("num1");
const numberTwoElem = document.getElementById("num2");
const resultElem = document.getElementById("result");

function clickBtnHandler() {
  resultElem.textContent =
    parseInt(numberOneElem.value) + parseInt(numberTwoElem.value);
}

btnElem.addEventListener("click", clickBtnHandler);
