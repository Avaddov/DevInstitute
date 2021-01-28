// Exercise 1 : Age Difference
// Given the birthdates of two people, find the date when the younger one is exactly half the age of the other.
// Notes: The dates are given in the format YYYY
let birthday1 = Number(prompt("What is your birth year?[YYYY]"));
let birthday2 = Number(prompt("What is your birth year?[YYYY]"));

let ageDiff = birthday1 - birthday2;
if (ageDiff < 0) {
  //birthday2 is older
  console.log(birthday2 - ageDiff);
} else {
  console.log(birthday1 + ageDiff);
}
