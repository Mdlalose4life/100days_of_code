#!/bin/bash
// JavaScript has Function scope and Glabal Scope.
function foo() {
    var par = 1;
    if (par = 1){
        var bar = 2;
        console.log(par);
        console.log(bar);
    }
    console.log(par);
    console.log(bar);
}
foo()