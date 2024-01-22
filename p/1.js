const ps = require("prompt-sync")
const prompt = ps()

// let a = prompt("Введи a")
// let b = prompt("Введи b")

function sum(a,b){
    return a + b
}

module.exports = {sum}