class HolbertonCourse{
    constructor (name, length, students){
        this._name = name;
        this._length = length;
        this._student = students
    }
    getName(){
        return this.name
    }

    getLength(){
        return this.length
    }
    getLength(){
        return this.students
    }   
}

const c1 = new HolbertonCourse("ES6", 1, ["Bob", "Jane"])
console.log(c1)