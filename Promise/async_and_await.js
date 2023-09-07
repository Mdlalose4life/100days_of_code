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

//let order = () => {
   // return new Promise((resolve, reject) => {
       // if(true){
         //   resolve()
       // }
       // else{
         //   reject()
      //  }
   // })
//}

async function order(){
    try{
        await abc
    }
    catch(error){
        console.log("abc does not exist", error)
    }
    finally{
        console.log("Runs code anyways")
    }
}
order()