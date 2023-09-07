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

let is_shop_open = false

function time(ms){
    return new Promise((resolve, reject) =>{
    if(is_shop_open){
        setTimeout(resolve, ms)
    }
    else{
        reject(
            console.log("We are closed")
        )
    }        
    })
}


async function kitchen(){
    try{
        await time(2000)
        console.log(`${stock.fruits[0]} fruite is selelcte`)

        await time(0)
        console.log("Production is started")

        await time(2000)
        console.log("Cutting the fruits")

        await time(1000)
        console.log(`${stock.liquid[0]} and ${stock.liquid[1]} is being addded`)

        await time(2000)
        console.log(`Start the machine`)

        await time(2000)
        console.log(`The ice cream is being put on ${stock.holder[0]} holder`)

        await time(3000)
        console.log(`The ${stock.topping[0]} topping is being choosen`)

        await time(2000)
        console.log("Ice Cream is served")
    }
    catch(error){
        console.log("customer left", error)
    }

    finally{
        console.log("Day is ended, shop is close")
    }
}
kitchen();