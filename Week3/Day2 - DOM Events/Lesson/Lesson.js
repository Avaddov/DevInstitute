// function clickParagraph() {
// 	console.log("hello")
// 	document.getElementById("p").classList.toggle("welcomeUser")




document.getElementById("p").onclick = function() {
	console.log("hello")
	document.getElementById("p").classList.toggle("welcomeUser")



    let container = document.getElementById("container")
for (let i = 0; i<3; i++){
	let p = document.createElement("p")
	let content = document.createTextNode("Hello")
	p.appendChild(content)
	container.appendChild(p)
}




function insert_Row(){
 
     
	var table = document.getElementById("sampleTable");
    // Find a <table> element with id="sampleTable":
​
​
	// Create an empty <tr> element and add it to the 1st position of the table:
	var row = table.insertRow(2);
​
	// Insert new cells (<td> elements) at the 1st and 2nd position of the "new" <tr> element:
	var cell1 = row.insertCell(0);
	var cell2 = row.insertCell(1);
​
	// Add some text to the new cells:
	cell1.innerHTML = "NEW CELL1";
	cell2.innerHTML = "NEW CELL2";
​
}
    



    function insert_Row() {
        // access the table
        let tableHtml = document.getElementById("sampleTable")
        //create a row
        let rowHtml = document.createElement("tr")
        //create 2 cells (or columns)
        for (let i = 0; i<2; i++){
            //create a column
            let columnHtml = document.createElement("td")
            //add text content to the column
            let contentCell = document.createTextNode(`Row New cell${i+1}`)
            //add the text node to the column
            columnHtml.appendChild(contentCell)
            //add the column to the row
            rowHtml.appendChild(columnHtml)
        }
        //add row to the table
        tableHtml.appendChild(rowHtml)
    }