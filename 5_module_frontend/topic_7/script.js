const number1 = document.getElementById("input1");
const number2 = document.getElementById("input2");

const resultElement = document.getElementById("result");

function clickHandler(event) {
  let operator = "btnPlus";
  let result = "Выберите оператора";

  operator = event.target.id;

  //   if (operator === "btnPlus") {
  //     result = parseInt(number1.value) + parseInt(number2.value);
  //   } else if (operator === "btnMinus") {
  //     result = parseInt(number1.value) - parseInt(number2.value);
  //   } else if (operator === "btnMul") {
  //     result = parseInt(number1.value) * parseInt(number2.value);
  //   } else if (operator === "btnDiv") {
  //     result = parseInt(number1.value) / parseInt(number2.value);
  //   }

  switch (operator) {
    case "btnPlus": {
      result = parseInt(number1.value) + parseInt(number2.value);
      console.log(result);
      break;
    }
    case "btnMinus": {
      result = parseInt(number1.value) - parseInt(number2.value);
      console.log(result);
      break;
    }
    case "btnMul": {
      result = parseInt(number1.value) * parseInt(number2.value);
      console.log(result);
      break;
    }
    case "btnDiv": {
      result = parseInt(number1.value) / parseInt(number2.value);
      console.log(result);
      break;
    }
  }

  //   console.log(result);
  resultElement.textContent = result;
}
