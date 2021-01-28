// Exercise 1 : Keyless Car
// Ask the user for his age, and save the value into a variable
// var age = Number(prompt('What is your age?'));
// // Create a function called checkDriverAge() that will alert the user if he can drive depending on his age.
// function checkDriverAge(age){

// }
// // if he is too young, alert “Sorry, you are too young to drive this car. Powering off”
// if (age < 18){
//     alert("Sorry, you are to young to drive. Powering off");
// // if he is old enough, alert “You are old enough to drive, Powering On. Enjoy the ride!”
// else if {
//     alert("Powering On. Enjoy the ride!");
// // if he just turned 18, alert “Congratulations on your first year of driving. Enjoy the ride!”
// }
// else (age == 18){
//     alert("Congratulations on your first year of driving. Enjoy the ride!");
// }
// Instead of using prompt to ask the user for his age, make the checkDriverAge() function accept an argument age,
//so that if you enter: checkDriverAge(92); it alerts “You are old enough to drive, Powering On. Enjoy the ride!”

//Exercise 2 

// Given a total due and an array representing the amount of change in your pocket, determine whether or not you are able to pay for the item.
// Change will always be represented in the following order: quarters, dimes, nickels, pennies.

// let myWallet = {
//   Quarters: 0.25,
//   Dimes: 0.10,
//   Nickels: 0.05,
//   Pennies: 0.01
// }
// function change([quarter, dime, nickel, penny], pay) {
//   let total = quarter*myWallet.Quarters + dime*myWallet.Dimes + nickel*myWallet.Nickels + penny*myWallet.Pennies;
//   if (pay <= total) {
//       return "true"
//   } else {
//       return "false"
//   }
// }

// let enough = change([25, 20, 5, 0], 4.25);
// console.log(enough);

// Exercise 3: Find The Multiples Of 23
// Write a js function that console.log the multiples of 23 less than 500 and at the end return the sum of all of them.

// let arrayNumber = [
//   0,
//   23,
//   46,
//   69,
//   92,
//   115,
//   138,
//   161,
//   184,
//   207,
//   230,
//   253,
//   276,
//   299,
//   322,
//   345,
//   368,
//   391,
//   414,
//   437,
//   460,
//   483,
// ];
// // Sum: 5313;
// function multiples() {
//   //create an array to hold numbers
//   let arrayNumber = [];
//   //loop through a range of numbers from 0 to 500
//   for (let number = 0; number <= 500; number++) {
//     //We check if the number is divisible by 23
//     //if the number is divible by 23
//     if (number % 23 == 0) {
//       //push the number into the array from before (arrayNumber)
//       arrayNumber.push(number);
//       //if the number is not divisible by 23
//     } else {
//       //skip this number
//       continue;
//     }
//   }
//   //makes the array accessible outside
//   return arrayNumber;
// }

// multiples();

// //Display the sum
// function sumNumbers() {
//   let listNumbers = multiples();
//   let sum = 0;
//   for (let i = 0; i < listNumbers.length; i++) {
//     sum += listNumbers[i];
//   }
//   console.log(`The sum is ${sum}`);
// }
// sumNumbers();

// OR;

// function multiples() {
//   const max_value = 500;
//   let max_lenght = max_value / 23;
//   console.log(max_lenght);
//   let elements = 0;
//   let sum = 0;
//   for (let i = 0; i < max_lenght; i++) {
//     elements += 23;
//     console.log(`Element ${i} is: ${elements}`);
//     sum += elements;
//   }
//   console.log(`My sum is: ${sum}`);
// }

// multiples();

// // Exercise 4 : Amazon Shopping
let amazonBasket = {
  glasses: 1,
  books: 2,
  floss: 100,
};
// Create a function called checkBasket().
function checkBasket() {
  // It should:
  // ask the user for the item he wants
  let itemRequest = glasses //prompt("What item do you want?")
  // and let him know if it’s in the basket or not
  // Hint: Use the in keyword inside the conditional
  if (itemRequest in amazonBasket){
    console.log(`You already have ${Object.amazonBasket} + ${amazonBasket} in your cart`);
}
}
