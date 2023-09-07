function setupNewUser(info, callback){
    var user = {
        name: info.name,
        nameLovercase: info.name.toLowerCase()
    };
    try {
        Database.save(user, callback)
    }
    catch(err){
        callback(err)
    }
}

/**
 *  We write Spies to collect information
 *  - sinon.assert.callCount - Retuns the number
 *  on how manya function was called.
 *  - sinon.assert.calledOnce - Retuns true if the function
 *  was called once. 
 *  */ 

// Verify that a function was called once.
it('It must be called once', function(){
    var save = sinon.spy(Database, 'save');

    setupNewUser({name: 'tesr'}, function() { });

    save.restore();
    sinon.assert.calledOnce(save)
})

it('it should pass objec with correct values to save', function() {
    var save = sinon.spy(Database, 'save');
    var info = {name: 'test'}
    var expectedUser = {
        name: info.name,
        nameLovercase: info.name.toLowerCase()
    }

    setupNewUser(info, function() { });


})