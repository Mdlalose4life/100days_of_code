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
let order  = (fruit_name, call_production) => {
    setTimeout(() => {
        console.log(`${stock.fruits[fruit_name]} was picked` );
    call_production();        
    }, 2000);

};

let production = () => {
    setTimeout(()=>{
        console.log("Production can now start");
        setTimeout(()=>{
            console.log("Cutting fruits has been completed")
            setTimeout(()=>{
                console.log(`${stock.liquid[0]} and ${stock.liquid[1]} is added`)
                
                setTimeout(()=>{
                console.log("Machine started")
                
                setTimeout(()=>{
                    console.log(`Icecream was placed on the ${stock.holder[0]}`)

                    setTimeout(()=>{
                        console.log(`${stock.topping[0]} topping was added as topping`)

                        setTimeout(()=>{
                            console.log("Ice cream is served")
                        },2000)
                    }, 2000)
                }, 2000)
            },1000)
            }, 1000)
        }, 2000)
    }, 0)
    };
order(1, production);