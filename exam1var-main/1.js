// let x = prompt("Введите значение х")
// let z = prompt("Введите значение z")

function sistem(x,z){
    if(Number.isNaN(Number(x)) || Number.isNaN(Number(z))){
        return "Вы ввели не число"
    }
    if(z <= 0){
        x = 1/(z*z+1)
        let y = x*(Math.log(x-1))
        y = y.toFixed(2)
        console.log(y)
        return y
    }
    else if(z > 0){
        x = 5*z
        let y = x*(Math.log(x-1))
        y = y.toFixed(2)
        console.log(y)
        return y
    }
}

// sistem(x,z)

module.exports = {sistem}