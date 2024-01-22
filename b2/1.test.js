const {z1} = require('./1')

describe('проверка',()=>{
    test('проверка значения',()=>{
        expect(z1(2,3)).toBe("39.59")
    })
})