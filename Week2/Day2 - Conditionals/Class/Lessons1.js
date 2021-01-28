// OBJECTS : access the element by the property
let user = {
	username : "John",
	password : 1234,
	email : "john@gmail.com",
	logIn : true,
	countries : ["israel", "usa"],
	friends : {
		names : ["David", "Sarah"]
	}
}
​
console.log(user)
// 1. display the friends nested object
​
// 2. display the list of names of his friends
​
// 3. display the name of best friend : David



// ARRAY OF OBJECTS
let users = [
	{
		username : "John",
		password: 1234
	},
	{
		username : "Lea",
		password: 2222
	},
	{
		username : "David",
		password: 6767
	}
];
​
console.log(users)
// 1. display the information of the 2nd user (object)
// 2. display the password of the 2nd user




// Make a keyless car!
// This car will only let you drive if you are over 18. Make it do the following:
// Using prompt() and alert(), ask a user for their age.
let age = Number(prompt('What is your age?'));

// IF they say they are below 18, respond with: "Sorry, you are too young to drive this car. Powering off
if (age < 18){
    alert("Sorry, you are to young to drive. Powering off");
}
// IF they say they are 18, respond with: "Congratulations on your first year of driving. Enjoy the ride!
else if (age == 18){
    alert("Congratulations on your first year of driving. Enjoy the ride!");
    // IF they say they are over 18, respond with: "Powering On. Enjoy the ride!"
} else {
    alert("Powering On. Enjoy the ride!");
}


// Write as comments the steps of the resolution of this piece of code

// Guess what will be the result before checking it


let a = 2 + 2;

switch (a) {
    //IF a = 3, respond 'Too small'
  case 3:
    alert( 'Too small' );
    break;
    //IF a = 4, respond 'Exactly!'
  case 4:
    alert( 'Exactly!' );
    break;
    //IF a = 4, respond 'Too large'
  case 5:
    alert( 'Too large' );
    break;
    //
  default:
    alert( "I don't know such values" );

    
    // Write as comments the steps of the resolution of this piece of code

    // Guess what will be the result before checking it


    let a = 2 + 2;

switch (a) {
  case 4:
    alert('Right!');
    break;

  case 3: // (*) grouped two cases
  case 5:
    alert('Wrong!');
    alert("Why don't you take a math class?");
    break;

  default:
    alert('The result is strange. Really.');
}