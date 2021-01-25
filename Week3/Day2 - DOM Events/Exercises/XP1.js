//get the p tags directly under the article element to make the pArr array
let pArr = document.querySelectorAll("article > p");
console.log(pArr); //progress-print

//iterate over the p-elements now in the pArr
for (let i = 0; i < pArr.length; i++) {
  pArr[i].classList.add("para_article"); //adding the para_article class to each item in pArr
}

pArr[pArr.length - 1].remove(); //remove the last item in pArr

//select the h2 element
let hElem2 = document.querySelector("h2");

//add an event listener that will remove h2 when it has been clicked on
hElem2.addEventListener("click", (ev) => {
  hElem2.remove();
});

//select the h1 element
let hElem1 = document.querySelector("h1");

//Set the font size of the h1 to be a random pixel size from 0 to 100.
function getRandomArbitrary(min, max) {
  return Math.random() * (max - min) + min;
}
hElem1.style.fontSize = getRandomArbitrary(0, 100) + "px";

// Hide the 1st paragraph, when it’s clicked. (use the display property )
pArr[0].addEventListener("click", (ev) => {
  pArr[0].style.display = "none";
});

// Get the values from the inputs and append them to the end of the html, inside a table.
let formElem = document.querySelector("form"); //get the form element
formElem.addEventListener("submit", (ev) => {
  //add the event for the submit button
  console.log("submit");
  let username = formElem.elements["userName"].value; //variable for username
  let question = formElem.elements["questionToUser"].value; //variable for QA
  let td1 = document.createElement("td"); //create table cell element1
  let td2 = document.createElement("td"); //create table cell element2
  td1.appendChild(document.createTextNode(username)); //add text to table cell
  td2.appendChild(document.createTextNode(question)); //add text to table cell
  let tr = document.createElement("tr"); //make table row
  tr.appendChild(td1); //add cell to row
  tr.appendChild(td2); //add cell to row
  let tbody = document.querySelector("tbody"); //get the tbody element
  tbody.appendChild(tr); //adding row to body
  ev.preventDefault(); //prevents refresh
});

//Bonus: Fade out the 2nd paragraph over 2000 milliseconds, when it’s clicked.
pArr[1].style.opacity = 1;
pArr[1].style.transition = "opacity 2000ms";
pArr[1].addEventListener("click", () => {pArr[1].style.opacity = 0;});
