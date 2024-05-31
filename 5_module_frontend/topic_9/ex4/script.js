const square = document.getElementById("square");

function clickHandler(event) {
  //   console.log(event);
  console.log(`x: ${event.clientX}, y: ${event.clientY}`);

  square.style.marginLeft = `${event.clientX - 50}px`;
  square.style.marginTop = `${event.clientY - 50}px`;
}

function timeoutHandler(event) {
  setTimeout(clickHandler, 50, event);
}

addEventListener("click", timeoutHandler);
