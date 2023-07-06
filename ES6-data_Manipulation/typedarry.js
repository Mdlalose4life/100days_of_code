let buffer = new ArrayBuffer(16) // Setting a buffer that allocate a 16 bytes of space per Number range (0 65535) 
let dv = new DataView(buffer) // Dataview allows you to perform oparations on a arraybuffer
let dv1 = new DataView(buffer, 4, 3) // Can have access to 4 bits from 10
 

dv1.setInt8(1, 50)

let num = dv1.getInt8(1)
console.log(num)