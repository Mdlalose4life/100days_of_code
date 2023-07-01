let stock ={
    fruits:[
        "grapes",
        "banana",
        "Strewberrys",
        "apples"
    ],
    liquid:[
        "Water",
        "ice"],
    holder:[ 
        "cone",
        "cup",
        "stick"
    ],
    topping:[
        "chocholate",
        "peanut"
    ]
};
let is_shop_open = true;

let order = (time, work) => {
    return new Promise((resolve, reject)=>{
        if (is_shop_open){
            setTimeout(()=>{
            resolve(work());                
            },time);
        }

        else{
            reject(console.log("The shop is closed"))
        }
    })
}
order(2000, ()=>console.log(`${stock.fruits[0]} was selected`))

.then(()=>{
    return order(0, ()=>console.log("Production has been started"))
})

.then(()=>{
    return order(2000, ()=>console.log("The cutting of fruits finished"))
})

.then(()=>{
    return order(1000, ()=>{
        console.log(`${stock.liquid[0]} and ${stock.liquid[1]} as selected`)
    })
})
.then(()=>{
    return order(1000,()=>console.log("starting the Machines"))
})
.then(()=>{
    return order(2000, ()=>{
        console.log( `The Ice crime is put on the ${stock.holder[0]}`)
    })
})

.then(()=>{
    return order(3000, ()=>{
        console.log(`Putting the ${stock.topping[1]} topping.`)
    })
})

.then(()=>{
    return order(1000, ()=>console.log("Ice cream is served"))
})


.catch(()=>{{
    console.log("Customer left")
}})

.finally(()=>{
    console.log("End of the day, shop is closed")
})