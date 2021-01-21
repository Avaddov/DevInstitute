// You’re given a string of words. You need to find the word “Nemo”, and return a string like this: “I found Nemo at [the order of the word you find nemo]!”.
// Bonus : If you can’t find Nemo, console.log “I can’t find Nemo :(“.
// Hint : use an if/else statement
// Examples
// "I am finding Nemo !" ➞ "I found Nemo at 4!"
// var sentence= "I am finding Nemo !"
// sentence=sentence.toLocaleLowerCase()
// var position= sentence.search("nemo")
// // var Nemo= sentence.split(" ")
// // var position= Nemo.indexOf("nemo")
// console.log("I found Nemo at " + position) 

  let string = "I am Nemo not a fish.";
    let split = string.split(" ");
    let n = split.indexOf("Nemo");
        if(n>0){
            console.log("I found Nemo at" + " " + n + "!");
        }
        else{
            console.log("Nemo is not here")
        }
