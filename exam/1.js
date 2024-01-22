const readline = require("readline")
const stra =
 readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

let a = "";
let b = "";
let c = "";

stra.question("введи a:", function (string) {
    a = string
    stra.question("введи b:", function (string) {
        b = string
        stra.question("введи a:", function (string) {
            c = string
            console.log(a,b,c);
            proverka(a,b,c)
            stra.close();
        });
    });
    // stra.close();
});

// proverka(1,1,1)
function proverka(a,b,c){
    // readline.question('введи a:', callback())
    // readline.question('введи b:', callback())
    // readline.question('введи c:', callback())

    if (a <= 0 || b <= 0 || c <= 0) {
        console.log("Это невозможный треугольник. Стороны треугольника не могут быть меньше или равны нулю");
        return "Это невозможный треугольник. Стороны треугольника не могут быть меньше или равны нулю"
    }
    if (a + b <= c || a + c <= b || b + c <= a) {
        console.log("Это невозможный треугольник. Сумма двух любых сторон треугольника не может быть меньше третьей");
        return "Это невозможный треугольник. Сумма двух любых сторон треугольника не может быть меньше третьей"
    }
    if (c ** 2 == a ** 2 + b ** 2){
        p = ((a + b + c) / 2)
        s1 = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        console.log("Треугольник прямоугольный \n Площадь = " + s1);
        return("Треугольник прямоугольный \n Площадь = " + s1)

    }
    if (c ** 2 < a ** 2 + b ** 2){
        p = ((a + b + c) / 2)
        s1 = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        console.log("Треугольник прямоугольный \n Площадь = " + s1);
        return("Треугольник прямоугольный \n Площадь = " + s1)

    }

    if (c ** 2 > a ** 2 + b ** 2){
        p = ((a + b + c) / 2)
        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        console.log("Треугольник остроугольный \n Площадь = " + str(s));
        return ("Треугольник остроугольный \n Площадь = " + str(s))

    }
}

module.exports = { proverka }
