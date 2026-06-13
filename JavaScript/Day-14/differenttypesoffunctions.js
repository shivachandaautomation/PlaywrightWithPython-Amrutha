//Function as an Expression

const multiply = function (a,b)
{
    c = a*b;
    return c
}

let result = multiply(606,98)

// console.log(result)

// Arrow function (ES6)
// shorter syntax for the writting functions
const add = (a,b) => {
    c = a+b
    return c
}

// single line arrow function
const add1 = (a,b) => a+b;

// console.log(add1(3,5))

const square1 = num => num * num;

// console.log(square1(5));

//Anonymous Function
// A function without a name

// setTimeout(function() {
//     console.log("Executed after 2 seconds");
// }, 2000);

//Executes immediately after creation.
// Immediately Invoked Function Expression (IIFE)

(function() {
    console.log("IIFE Executed");
})();

// Default Parameters

function greet (name = "Guest")
{
    console.log("Hello" + name)
}

// greet("Amrutha")

// Rest parameters
// Allow a function to accept multiple arguments


function sum(...numbers) {
    return numbers.reduce((total, num) => total + num, 0);
}

console.log(sum(10, 20, 30, 40));

