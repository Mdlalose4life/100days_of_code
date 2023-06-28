#!/usr/bin/env
// Local and global scope
var num = 10;
function test(){
    var num = 100;
    console.log("value of num inside test()"+num)
}
console.log("value of num outside the test()"+num)
test()