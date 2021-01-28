// function(add){}
// function(multiply){}
// function(subtract){}
// function(divide){}
let calcDisplay = document.getElementById("display"); //html source
// console.log(calcDisplay) //
let calcstr = "";

//fetches the info from the HTML to make the buttons function upon being clicked.
function buttonclick(btn) {
  calcstr = calcstr + btn;
  calcDisplay.innerHTML = calcstr;
  // console.log(calcDisplay)
}
//function for the = button using the eval function to sum up what is being desplayed in the string.
function result() {
  let calcresult = eval(calcstr);
  calcDisplay.innerHTML = calcresult;
}
//function for the clear button to reset the string back to 0.
function reset() {
  calcstr = "";
  calcDisplay.innerHTML = 0;
}

//Removes the last number added to input by measuring the current length -1
//(making it function as a backspace. If nothing has been inputed, it stays as 0)
function remove() {
  if (calcDisplay.innerHTML.length > 1) {
    calcDisplay.innerHTML = calcDisplay.innerHTML.slice(0, -1);
  } else {
    calcDisplay.innerHTML = 0;
  }
}
