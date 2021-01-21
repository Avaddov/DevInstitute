// // Exercise 1 : Your Favorite Colors
// // Create an array to hold your top colors.
// let colors = ["red", "black", "green"]; // colors
// // For each choice, console.log a string like: “My #1 choice is blue”
// // Bonus: Change it to console.log “My 1st choice”, “My 2nd choice”, “My 3rd choice”, picking the right suffix for the number.
// const suffixes = ["st", "nd", "rd"];
// // Hint : create an array of suffix to do the Bonus
// colors.forEach((color, i) => {
//   console.log("My " + (i + 1) + suffixes[i] + " favorite color is " + color); //output
// });

// // Exercise 2 : List Of People
// let people = ["Greg", "Mary", "Devon", "James"];
// // Using a loop, iterate through this array and console.log all of the people.
// for (const i in people) {
//   console.log(people[i]);
// }
// // Write the command to remove “Greg” from the array.
// people.shift();
// console.log(people);
// // Write the command to replace “James” by “Jason” in the array.
// let jamesIdx = people.indexOf("James");
// if (jamesIdx !== -1) {
//   people.splice(jamesIdx, 1);
// }
// people.push("Jason");
// console.log(people);
// // Write the command to add your name to the end of the array.
// people.push("Dov");
// console.log(people);
// // Using a loop, iterate through this array and after console.log-ing “Mary”, exit from the loop.
// let maryIdx = people.indexOf("Mary");
// for (i = 0; i < people.length; i++) {
//   console.log(people[i]);
//   if (i == maryIdx) {
//     break;
//   }
// }
// // Write the command to make a copy of the array using slice. The copy should NOT include “Mary” or your name.
// let newPeople = people.slice(1, 3);
// console.log(newPeople);
// // Write the command that gives the indexOf where “Mary” is located.
// console.log(people.indexOf("Mary"));
// // Write the command that gives the indexOf where “Foo” is located (this should return -1).
// console.log(people.indexOf("Foo"));
// // Write a variable called last which value is the last element of the array.
// let last = people.pop();
// console.log(last);
// // Hint: What is the relationship between the index of the last element in the array and the length of the array?

// Exercise 3 : Repeat The Question
// Ask a number to the user, while the number is smaller than 10, ask him for a new number.
// var num = 0;
// // Tip : Which while loop is more relevant for this situation?
// while (num < 10) {
//  num = Number(prompt("pick a number"));
// }

// Exercise 4 : Attendance
// Suppose you have a guest list of students and the country they are from,
//stored as key-value pairs in an object. You have to make the attendance.

// let guestList = {
//   Randy: "Germany",
//   Karla: "France",
//   Wendy: "Japan",
//   Norman: "England",
//   Sam: "Argentina",
// };
// // Ask the student for his name :
// let studentName = prompt("What is your name?");
// // If the name is in the object, console.log the name of the student and the country he comes from.
// // "Hi! I'm [name], and I'm from [country]."
// var keys = Object.keys(guestList);
// if (studentName in guestList) {
//   console.log(
//     "Hi! I'm " + studentName + " , and I'm from " + guestList[studentName]
//   );
//   // If the name is not in the object, console.log :"Hi! I'm a guest."
// } else {
//   console.log("Hi, I'm a guest.");
// }

// Exercise 5 : Family
// Create an object called family with a few properties.
let family = {
  mother: "Gabriella",
  father: "Michael",
  children: 3,
  isMarried: true,
  city: "Jerusalem",

  // Display only the properties. (using a for loop)
};
for (const i in family) {
  console.log(i);
}
// Display only the values. (using a for loop)
for (const j in family) {
  console.log(family[j]);
}

// // // Exercise 6 : Secret Group
// let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
// // // A group of friends have decided to start a secret society.
// // // The society’s name will be the first letter of each of their firstnames, sorted in alphabetical order.
// let sort = names.sort(); //sort names into a new array
// console.log(sort);
// let letters = ""; //new string to store the first letters of each name
// for (i in sort) {
//   letters += sort[i][0]; //itterate over the names and add the first[0] index of each one into the previously empty string
// }
// console.log(letters); //print the newly filled string
// // // Console.log the name of their secret society.
