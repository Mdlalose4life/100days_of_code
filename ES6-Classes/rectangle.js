class Rectangle{
    //Setup the objects
    constructor (_width, _height, _color){
        this.width = _width;
        this.height = _height;
        this.color = _color;
    }
    getArea (){
        return this.width * this.height
    }

    printDescription () {
        console.log(`A Rectangle of height ${this.height}, ${this.width} width and ${this.color} color`);
    }
}

//create an object of a class
let myRectangle = new Rectangle(5, 7, "blue");
let myRectangle1 = new Rectangle(10, 4, "Red");

//Printing the objects instanse
myRectangle.printDescription()
console.log(myRectangle.getArea())
myRectangle1.printDescription()
console.log(myRectangle1.getArea())
