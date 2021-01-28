// // Ask a user for several words (separated by commas).
// let words = "I,Am,A,Potato."; //prompt("Type some words. (seperated by commas)");
// // Push the words into an array.

// // Console.log them, one per line, in a rectangular frame.

function wordFrameBuilder(sentence) {
  // let sentence = 'hello world in a frame';
  let sentenceArray = sentence.split(" ");
  // console.log(sentenceArray);

  //use the longest word to base where the stars should be positioned
  let word = "";
  let longest = "";
  //find the longest word
  for (word of sentenceArray) {
    if (word.length > longest.length) {
      longest = word;
    }
  }
  //get the length of the longest word
  let length = longest.length;
  let stars = "";
  for (let i = 0; i < length; i++) {
    stars = stars.concat("*");
  }
  // console.log(stars);

  //place the stars on the top and bottom rows based on the length of the longest word
  let topAndBottom = "**" + stars + "**";
  // console.log(longest);
  console.log(topAndBottom);
  for (word of sentenceArray) {
    let spaceLength = length - word.length;
    let space = "";
    for (let x = 0; x < spaceLength; x++) {
      space = space.concat(" ");
    }
    console.log("* " + word + space + " *");
  }
  console.log(topAndBottom);
}
wordFrameBuilder(prompt("please enter a sentence"));
