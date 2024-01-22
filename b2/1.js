const ps = require('prompt-sync')
const prompt = ps()

let x = prompt("введите x :")
let z = prompt("введите z :")

function z1(x,z){
    if(z <=0){
        x = 1/(Math.pow(z,2)+1)
        let y = x*(Math.log(x-1))
        y = y.toFixed(2)
        return y
    }
    else{
        x = 5*z
        let y = x*(Math.log(x-1))
        y = y.toFixed(2)
        return y
    }
}

module.exports = {z1}