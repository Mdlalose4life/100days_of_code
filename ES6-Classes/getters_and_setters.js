class Square {
    constructor(_width) {
        this.width = _width;
        this.height = _width;
        this.numOfRequestsForAre = 0;
    }
    // Getter
    get area () {
        this.numOfRequestsForAre++;
        return this.width * this.height
    }
    // Setter
    set area (area) {
        this.width = Math.sqrt(area);
        this.height = this.width
    } 
}
let Square1 = new Square(3)
//Printeing the getter
//console.log(Square1.area)

//Printing the Setter
//Square1.height = 2
console.log(Square1.area)
console.log(Square1.area)
console.log(Square1.area)
console.log(Square1.area)
console.log(Square1.area)
console.log(Square1.area)

console.log(Square1.numOfRequestsForAre)