// Exercise 1 : Change The Navbar


// let navBar = document.getElementById("navBar");
// console.log(navBar);
// navBar.setAttribute("id", "socialNetworkNavigation");

// let ul = document.getElementsByTagName("ul")[0]; // access the ul in the html (the only one)
// console.log(ul);

// let liNew = document.createElement("li"); // access li
// let anchor = document.createElement("a"); //access a tag
// let att = document.createAttribute("href"); //access href
// att.value = "#";
// anchor.setAttributeNode(att);
// let text = document.createTextNode("Logout"); //assign text
// anchor.appendChild(text);
// liNew.appendChild(anchor);
// ul.appendChild(liNew);
// //access ul
// console.log(liNew);



// // EXERCISE 2

// // 1. access second li 

// let ul = document.body.firstElementChild.nextElementSibling // access first ul

// let li = ul.lastElementChild // access first li


// // 2. change name

// let liTwo = document.getElementsByTagName('li')[1].innerHTML='Richard';
// console.log(liTwo);

// let collection = document.getElementsByTagName('li').length;   //grabbing all li to find out how many li we have
// //console.log(collection);

// for (let i = 0; i <collection; i++){
//     let liTwo = document.getElementsByTagName('li')[i].innerHTML='Dov';
// }






// let ulTwo = document.getElementsByTagName('ul');

// for (let selectedUl of ulTwo) {
//     selectedUl.firstElementChild.innerHTML = 'Dov'
//     console.log(selectedUl.firstElementChild.innerHTML);
// }


// option 2 - first (li) inside the (ul)

let allUl = document.getElementsByTagName('ul');


for (let selectedUl of allUl ){
    selectedUl.firstElementChild.innerHTML = 'Dov'
    let liNew = document.createElement('li'); //3. created a new 'li'   //='Hey Students'  
    let text = document.createTextNode('Hey Student!') //3. create text
    liNew.appendChild(text); //3. appendChild to liNew
    selectedUl.appendChild(liNew); //3. appendChild to selectedUl
    
}

