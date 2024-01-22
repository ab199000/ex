const {sum} = require("./1")

describe("проверка1",()=>{
    test("сумма",()=>{
        expect(sum(1,2)).toBe(3)
        expect(sum(1,4)).toBe(5)
        expect(sum(1,5)).toBe(6)
    })
})