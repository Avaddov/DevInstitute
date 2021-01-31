// STEP 1) create Sidebar clear button & divs (21)
// access container & sidebar div
// let sidebar = document.getElementById('sidebar') 
​ 
​
let sidebar = document.getElementById('sidebar')
//console.log(sidebar);
​
​
// create Clear Button
let btn = document.createElement('button');
btn.innerHTML = 'Clear';
​
btn.setAttribute('onclick', clear()) //set button attribute to onclick - execute function clear
​
sidebar.appendChild(btn);
​ 
function clear (){
​
}
​
​
// create color divs
let colors = ['red', 'orangered', 'orange', 'yellow', 'yellowgreen', 'lightgreen', 'green', 'turquoise', 'cyan', 'lightblue', 'dodgerblue', 'blue', 'darkblue', 'indigo', 'darkmagenta', 'violet', 'pink', 'lightgrey', 'grey', 'black', 'white']
​
for (let i = 0; i < colors.length; i++){
    let newDiv = document.createElement('div');
    sidebar.appendChild(newDiv)
    newDiv.className = ('color');
    newDiv.style.backgroundColor = colors[i];
    newDiv.style.height = '50px'
    newDiv.style.width = '50px'
    newDiv.style.border = '2px solid black'
    newDiv.style.margin = '2px'
    
}