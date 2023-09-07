const { error } = require('console')
const fs = require('fs')

// Reading a file
// fs.readFile('./docs1/database.txt', (err, data) =>{
//    if (err){
//        console.log(err)
//   }
//    console.log(data.toString())
// })
// console.log('Asynchronious way')

// Writting a file
// fs.writeFile('./docs/database.txt', 'I relaplce all with this' , () => {
// console.log("Success")
// })

// directories
// if (!fs.existsSync('./myfile')) {
//    fs.mkdir('./myfile', (error) => {
//    if(error) {
//       console.log(error)
//    }
//    console.log('Folder created')
//    })
// } else {
//    fs.rmdir('./myfile', (err) => {
//        if (err) {
//            console.log(err)
//        }
//        console.log('folder is removed')
//    })
// }

// delete files
// if (fs.existsSync('./docs/delete.txt')){
//     fs.unlink('./docs/delete.txt', (err) => {
//         if (err) {
//             console.log(err)
//         }
//         console.log('File is deleted')
//     })
//}

console.log(fs)