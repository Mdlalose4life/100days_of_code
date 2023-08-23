const { add, sub } = require('../src/app')
const expect =  require('chai').expect

// DBB
describe('add', () => {
    it('add(5, 5) must result to 10', () => {
        expect(add(5, 5)).to.be.equal(10)
    })
})