// 5 >= 1
//     0 === 1
//     4 <= 1
//     1 != 1
//     "A" > "B"
//     "B" < "C"
//     "a" > "A"
//     "b" < "A"
//     true === false
//     true != true

// console.log(5>=1) true
// console.log( 0 === 1) false
// console.log( 4 <= 1) false
// console.log(1 != 1) false
// console.log("A" > "B") false
// console.log("B" < "C") true
// console.log("a" > "A") true
// console.log( "b" < "A") false
// console.log (true === false) false
// console.log ( true != true) false

// EXERCISE 2
// let c;
// let a = 34;
// let b = 21;
// a = 2;
// a + b
// What will return a + b?
// What is the variable c equal to?
// Analyse the code below without running it, what will be the output ?
// console.log(a+b)
// Q: What will return a + b? A: 23
// Q: What is the variable c equal to? A: undefined
// Q: Analyse the code below without running it, what will be the output ?
// console.log(3 + 4 + '5');

//EXERCISE 3

//Ask the user for a string of numbers separated by a comma and space, return the product of the numbers.
//Hint: use some string methods

// Examples
// "2, 3"➞ 6
// var numbers= prompt("pick 2 numbers to add using a comma and space")
// var slice=numbers.split(", ")
// console.log(slice[0]*slice[1])
// alert((slice[0]*slice[1]))


// EXERCISE 4 : Boom
// Hint: if statement (tomorrow’s lesson)
// Ask the user for a number, return a string of the word “Boom”, which varies in the following ways:

// The string should include n number of “o”s, unless n is below 2 (in that case, return “boom”).
// If n is evenly divisible by 2, add an exclamation mark to the end.
// If n is evenly divisible by 5, return the string in ALL CAPS.
// If n is evenly divisible by both 2 and 5, return the string in ALL CAPS and add an exclamation mark to the end.
// The example below should help clarify these instructions.
// Examples
// 4 ➞ "Boooom!"
// // There are 4 "o"s and 4 is divisible by 2 (exclamation mark included)
// 1 ➞ "boom"
// // 1 is lower than 2, so we return "boom"

// var num = Number(prompt("pick a number"));
// var boom;
// if (num > 2) {
//   boom = "b" + "o".repeat(num) + "m";
// } else {
//   boom = "boom";
// }
// if (num % 2 == 0) {
//   boom = boom + "!";
// } else if (num % 5 == 0) {
//   boom = boom.toUpperCase();
// }
// console.log(boom);
// alert(boom)
