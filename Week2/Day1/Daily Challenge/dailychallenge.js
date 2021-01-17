let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];


// Remove the Banana from the array.
fruits.shift();
console.log(fruits)
// Sort the array in order.
fruits.sort();
console.log(fruits)
// Put “Kiwi” at the end of the array.
fruits.push("Kiwi");
console.log(fruits)
// Remove “Apples” from the array. Don’t use the same method as in the question 1.
fruits.splice(0,1);
console.log(fruits)
// Sort the array in reverse order. (Not alphabetical, but reverse the current Array i.e. [‘a’, ‘c’, ‘b’] becomes [‘b’, ‘c’, ‘a’])
fruits.reverse();
console.log(fruits)
// You should have at the end:
// let fruits = ["Kiwi", "Oranges", "Blueberries"];
