const {sistem} = require('./1')

describe('Проверка правильных значений', () => {
    test('Положительные значения',()=>{
        expect(sistem(34,50)).toBe('1379.36')
    })
});
