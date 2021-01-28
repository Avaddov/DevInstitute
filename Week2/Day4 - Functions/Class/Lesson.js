//1

// 1. Create a structured html file linked to a js file

// 2. Write a JS function that takes a parameter: myAge
function age(myAge) {
  let momAge = 2 * myAge;
  let dadAge = 1.2 * momAge;
  console.log(
    `my mom is ${momAge} years old and my dad is ${ageDad} years old`
  );
}
// 3. Console.log the age of my mum and my dad (my mum is twice my age, and my dad is 1.2 the age of my mum)

// 4. Call the function



//2
// Local & Global scope

//global variable
// decared in the global scope
let username = "Lea"
​
console.log("1:", username) // display Lea
​
//DECLARING
function familyAge (myAge) {
	console.log("2:",username) // display Lea
	// In the local scope I can modify a
	// variable that was declared in the global scope
	// and I can change the global variable
	username = "David"
	console.log("3:",username) // display David
	//local variables
	let ageMum = myAge*2
	let ageDad = ageMum*1.2
	console.log(`The age of my mum is ${ageMum}, the age of my dad is ${ageDad}`)
}
​
//INVOKE
familyAge(60)
​
console.log("4:",username) // display David
​

​
​
//global scope
console.log(ageMum) // undefined
​
// // LOCAL VARIABLE: IS A VARIABLE DECLARED IN THE LOCAL SCOPE
// // YOU CANNOT ACCESS A LOCAL VARIABLE IN THE GLOBAL SCOPE





//3
// Declaring & Invoking a function

// declaring a function
				// PARAMETERS
                function userInfo (username,age,height) {
                    console.log("Hello " + username)
                    console.log("Age " + age)
                    console.log("Height " + height)
                }
                ​
                //global scope
                console.log("username :", username)
                ​
                // Local means used in the local scope : in a block
                // functions, loops, conditionals
                ​
                // Global means used in the global scope
                // outside of a local
                ​
                ​
                // invoke/call the function
                // ARGUMENT
                userInfo("David",25, 1.7)