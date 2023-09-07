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

let is_shop_open = true

let topping_choice = () => {

    return new Promise( (resolve, reject)=>{ 
        setTimeout(()=>{
            resolve(
            console.log("Which topping would you like ?")
            )
        }, 3000)
    })
}

async function kitchen () {
    console.log("A")
    console.log("B")
    console.log("C")

    await topping_choice()

    console.log("D")
    console.log("E")
}
kitchen()
console.log("doing dishes")
console.log("Cleaning tables")
console.log("taking orders")