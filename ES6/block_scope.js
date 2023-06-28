"Strict"
function test()
{
    var num = 100;
    console.log("value of num in test() "+num)
    {
        console.log("Inner block")
        let numb = 30
        console.log("value of num: "+numb)
        console.log("Var num could be accessed here too "+num)
    }
}
test()