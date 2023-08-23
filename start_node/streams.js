const fs = require('fs');

const readstream = fs.createReadStream('./docs/stream.txt', { encoding: 'utf-8' });
const writestream = fs.createWriteStream('./docs/write_stream.txt')

// readstream.on('data', (chunk) => {
//     console.log('------ NEW CHUNK -------');
//    writestream.write('\n --- CHUNK ---  \n');
//    writestream.write(chunk);
//});

// Pipe
readstream.pipe(writestream)