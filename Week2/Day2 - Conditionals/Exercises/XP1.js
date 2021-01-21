// Exercise 1: Simple If/Else Statement

// Create 2 variables, x and y. Each of them has a different numeric value.
// let x = 5;
// let y = 3;
// // Write an if/else statement that checks the biggest number.
// if (x > y) {
//   console.log("x is the bigger number");
// } else if (y == x) {
//   console.log("x and y are equal");
// } else {
//   console.log("y is the bigger number");
// }

// // Exercise 2: Chihuahua
// // Create a variable newDog that is equal to the string “Chihuahua”.
// let newDog = 'Chihuahua'
// // Check and display how many letters are in newDog.
// console.log(newDog.length)
// // Display the newDog variable in uppercase and then in lowercase (no need to create new variables, just use 2 console.log).
// console.log(newDog.toUpperCase())
// console.log(newDog.toLowerCase())
// // Check if the variable newDog equals to “Chihuahua”
// if(newDog == 'Chihuahua'){
// // if it does, display ‘I love Chihuahuas, they're my favorite dog breed.’ (That is a lie. I hate Chihuahuas.)
// console.log("I love Chihuahuas, they're my favorite dog breed.")
// // else, console.log ‘I prefer cats.’
// } else {
//     console.log("I prefer cats.")
// }

// Exercise 3: Even Or Not Even

// Ask a number to the user, and save it to a variable.
let num = Number(prompt("Pick a number"));
// Check if the variable is an even number
if (num % 2 == 0) {
  // If it is, display: “x is an even number’. Where x is the actual number of the user.
  console.log("x is an even number");
  alert("x is an even number");
  // If it isn’t, display “x is not an even number’. Where x is the actual number of the user
} else {
  console.log("x is an odd number");
  alert("x is an odd number");
}

// // Exercise 4: Group Chat
// let users = [
//   "Lea123",
//   "Princess45",
//   "cat&doglovers",
//   "helooo@000",
//   "n00bmaster69420",
// ];
// let numberOfUsers = users.length;
// let numberOfRemainingUsers = numberOfUsers - 2;
// // Using the array above, console.log the number of users in a group conversation based on the following rules:
// // If there is no one, display “no one is online”.
// if (users.length == 0) {
//   console.log("no one is online");

//   // If there is 1 person, display “<name_user> is online”.
// } else if (users.length == 1) {
//   console.log(users[0] + " is online"); //gets first index of online user
//   // If there are 2 people, display “<name_user1> and <name_user2> are online”.
// } else if (users.length == 2) {
//   console.log(users[0] + " " + users[1] + " are online");
//   // If there are n>2 people, display the first two names and add “and n-2 more are online”.
// } else if (users.length > 2) {
//   console.log(
//     users[0] +
//       ", " +
//       users[1] +
//       " and " +
//       numberOfRemainingUsers +
//       " more are online"
//   );
// }
// For example, if there are 5 users, it should display:
// name_user1, name_user2 and 3 more are online
