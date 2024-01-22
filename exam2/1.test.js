const { main, perimetr, squer } = require('./1')

describe("Проверка периметра", ()=>{
    test("Проверка на отрицательные значения", ()=>{
         expect(perimetr(-2,-6)).toBe("Сторона не может быть отрицательной")
    })
    test("Проверка на положительные значения", ()=>{
         expect(perimetr(4,3)).toBe(12)
    })
})

describe("Проверка площади",()=>{
    test("Проверка на отрицательные значения",()=>{
        expect(squer(-2,-6)).toBe("Сторона не может быть отрицательной")
    })
    test("Проверка положительных значений",()=>{
        expect(squer(4,3)).toBe(6)
    })
})

describe("Проверка сложения периметров", ()=>{
    test("Правильновведенные значения", ()=>{
        expect(main([1,2],[3, 4])).toEqual([ 17.24, 7 ])
    })
    test("строки значения", ()=>{
         expect(main(['g','e'],['c','v'])).toBe("Было введено не чило")
    })
    test("лишнее значение", ()=>{
         expect(main('1 2 2','3 4')).toBe("Вы не ввели два значения")
    })
})