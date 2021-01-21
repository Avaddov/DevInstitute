// Exercise 1 : The World Translator
// Hint: Use Switch Case

// Ask the user which language he speaks.
let language = prompt("what language do you speak?");
// Create a few conditions :
switch (language) {
  // If he speaks French : display “Bonjour”
  case "French":
    console.log("Bonjour");
    break;
  // If he speaks English : display “Hello”
  case "English":
    console.log("Hello");
    break;
  // If he speaks Hebrew : display “Shalom”

  case "Hebrew":
    console.log("Shalom");
    break;
  // If he doesn’t speak none of these 3 languages: display ‘01110011 01101111 01110010 01110010 01111001’
  default:
    console.log("01110011 01101111 01110010 01110010 01111001");
}

// // Exercise 2 : The Grade Assigner
// // Ask the user for his grade
// let grade = prompt("What is your score?");
// // If the score is bigger than 90, console.log “A”
// if (grade > 90) {
//   console.log("A");
//   // If the score is between 80 and 90 (included), console.log “B”
// } else if (grade > 80 && grade <= 90) {
//   console.log("B");
//   // If the score is between 70(included) and 80 (included), console.log “C”
// } else if (grade > 69 && grade <= 80) {
//   console.log("C");
//   // If the score is lower than 70, console.log “D”
// } else {
//   console.log("D");
// }

// // Exercise 3 : Verbing
// // Create a variable, it must be a verb.
// var word = "swim";
// // If the length of this string is at least 3, it should add ‘ing’ to its end, unless it already ends in ‘ing’, in which case it should add ‘ly’ instead.
// if (word.length >= 3) {
//   // If the string length is less than 3, it should leave it unchanged.
//   if (word.endsWith("ing")) {
//     // Example:
//     // The string is : "swim" , your program should console.log : "swimming"

//     // The string is : "swimming", your program should console.log : "swimmingly"
//     word = word + "ly";
//   } else {
//     word = word + "ing";
//   }
// }
// // The string is : "go" your program should console.log : "go"
// console.log(word);
