// Instructions
// Write a JavaScript program to recreate the pattern below
// Hint: use nested for loop.
// Do this Daily Challenge by youself, without looking at the answers on the internet
// *
// * *
// * * *
// * * * *
// * * * * *
// * * * * * *

let star = ["*", "* * ", "* * *", "* * * *", "* * * * *", "* * * * * *"];
for (let i = 1; i <= 6; i++) {
  //goes over each element

  console.log("* ".repeat(i)); //and prints each one on a separate line till it reaches the end of the for loop
}
