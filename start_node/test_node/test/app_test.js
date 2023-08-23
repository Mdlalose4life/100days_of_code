const assert = require('chai').assert;
const app = require('../app');

describe('App', function() {
    it('greet should return Hello Pum Pum', function() {
        let result = app.greet()
        assert.equal(result, 'Hello Pum Pum');
    });

    it('greet should return retun type string', function() {
        let result = app.greet()
        assert.typeOf(result, 'string')
    });

    it('addNum results to a number above 5', function() {
        let result = app.addNum(4, 5)
        assert.isAbove(result, 5);
    })

    it('greet should return retun type string', function() {
        let result = app.addNum()
        assert.typeOf(result, 'number')
    });
});