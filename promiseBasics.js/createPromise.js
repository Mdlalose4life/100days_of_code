var promise = new Promise(function(resolve, reject){
    //The woring mechansms
    if(!Error/*Everything turns out to be fine*/){
        resolve("Hhhhey congratulatins")
    }
    else{
        reject(Error("Something did not work"))
    }
})