let buffer = new ArrayBuffer(4);
let uint8Array = new Uint8Array(buffer);

uint8Array[0] = 10;
uint8Array[1] = 20;
uint8Array[2] = 30;
uint8Array[3] = 40;

console.log(uint8Array)