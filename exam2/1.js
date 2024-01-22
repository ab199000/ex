function perimetr(a,b){
    let c = Math.sqrt(Math.pow(a,2) + Math.pow(b,2))
    if(a < 0 || b < 0){
        return "Сторона не может быть отрицательной"
    }
    return Number(a+b+c)
}
// perimetr(4,3)
function squer(a,b){
    if(a < 0 || b < 0){
        return "Сторона не может быть отрицательной"
    }
    return Number(1/2 * (a*b))
}
// squer(4,4)

const ps = require("prompt-sync")
const prompt = ps()

// let triangle1 = prompt("Введите катеты первого треугольника: ").split(' ')
// let triangle2 = prompt("Введите катеты второго треугольника: ").split(' ')

function main(triangle1,triangle2){

    if(triangle1.length != 2 || triangle2.length != 2){
        console.log('Вы не ввели два значения');
        return "Вы не ввели два значения"
    }

    if(Number.isNaN(Number(triangle1[0])) || Number.isNaN(Number(triangle1[1])) || Number.isNaN(Number(triangle2[0])) || Number.isNaN(Number(triangle2[1]))){
        console.log("Было введено не чило");
        return 'Было введено не чило'
    }

    let sumPerimtr = perimetr(Number(triangle1[0]),Number(triangle1[1])) + perimetr(Number(triangle2[0]),Number(triangle2[1]))

    sumPerimtr = sumPerimtr.toFixed(2)

    let sumSquer = squer(Number(triangle1[0]),Number(triangle1[1])) + squer(Number(triangle2[0]),Number(triangle2[1]))
    sumSquer = sumSquer.toFixed(2)
    console.log('Сумма периметров: ' + sumPerimtr);
    console.log('Сумма площадей: ' + sumSquer);
    console.log([Number(sumPerimtr),Number(sumSquer)]);
    return [Number(sumPerimtr),Number(sumSquer)]
    // return console.log({sumPerimtr,sumSquer});
}

// let sum = main(triangle1,triangle2)

// main()
// console.log(25 ** 0.5);

module.exports = {main, perimetr, squer}