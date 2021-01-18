// Exercise 1 : Your Favorite Colors
// Create an array to hold your top colors.
let colors = ["red", "black", "green"]; // colors
// For each choice, console.log a string like: “My #1 choice is blue”
// Bonus: Change it to console.log “My 1st choice”, “My 2nd choice”, “My 3rd choice”, picking the right suffix for the number.
const suffixes = ["st", "nd", "rd"];
// Hint : create an array of suffix to do the Bonus
colors.forEach((color, i) => {
  console.log("My " + (i + 1) + suffixes[i] + " favorite color is " + color); //output
});
//loop to determine position

// Exercise 2 : Secret Group
// let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"]
// A group of friends have decided to start a secret society. The society’s name will be the first letter of each of their firstnames, sorted in alphabetical order.
// Console.log the name of their secret society.

// let people = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"]; // names
