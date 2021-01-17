let str1 = 'pod'; 
let str2 = 'mix';
// let str4= str1.substring(0,string1.length()-1) +str2.substring(str2.length()-1)
let newWord= str1.slice(0,2) + str2.slice(2) + " " + str2.slice(0,2) + str1.slice(2);
console.log(newWord)