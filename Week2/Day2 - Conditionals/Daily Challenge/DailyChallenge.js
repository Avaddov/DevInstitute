// Instructions
// Daily Challenge : Not Bad
// Create a string that has the word “not” and “bad” inside
let str1 = "Persona5 is not a bad game";
// Create another variable that should find the first appearance of the substring “not” and “bad”.
let wordsArr = str1.split(" "); // this splits the string at the spaces and puts it into an array so it can be indexed properly
console.log(wordsArr);
// If the ‘bad’ follows the “not”, then it should replace the whole “not”…”bad” substring with ‘good’ then console.log the result.
let notIdx = wordsArr.indexOf("not"); //this locates the index of the word "not"
let badIdx = wordsArr.indexOf("bad"); //this locates the index of the word "bad"
let wordsBetweenCount = badIdx - notIdx;
console.log(wordsBetweenCount);
// If it doesn’t find “not” and “bad” in the right sequence (or at all), just console.log the original sentence.
if (notIdx < badIdx) {
  //meaning the index number, meaning that not comes before bad
  wordsArr.splice(notIdx, wordsBetweenCount + 1, "good");
  //Starts at index of not, then counts the words between not and bad(inclusive) and replaces them with "good"

  //merge back into string
  console.log(wordsArr.join(" "));
} else {
  console.log(str1);
}

// Example:

//   Your string is : 'This dinner is not that bad!', the result is : 'This dinner is good!'
//   Your string is : 'This movie is not so bad!' the result is : 'This movie is good!'
//   Your string is : 'This dinner is bad!' the result is : 'This dinner is bad!'
