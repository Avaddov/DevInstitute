//1st step : set the attribute draggable to true
let hello = document.getElementById("box");
hello.setAttribute("draggable", "true");
hello.addEventListener("dragstart", dragHello);
function dragHello(event) {
  console.log(event.clientX);
}
hello.addEventListener("dragend", dropHello);
function dropHello(event) {
  let horizontal = event.clientX;
  let vertical = event.clientY;
  event.target.style.left = horizontal + "px";
  event.target.style.top = vertical + "px";
  event.target.style.position = "absolute";
  console.log(horizontal);
}
