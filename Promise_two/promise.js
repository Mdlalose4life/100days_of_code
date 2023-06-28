const posts = [
    {title: 'Post One', body: "The begganing of life" },
    {title: 'Post two', body: "Cycle under the sun" }
];

function getPosts(){
    setTimeout(()=>{
        let output = '';
        posts.forEach((posts, index)=>{
            output = `${posts.title} - ${posts.body}`;
            console.log(output)
        })

    }, 1000)
}


function createPost(post){
    return new Promise((resolve, reject)=>{
    setTimeout(() => {
        posts.push(post);

        const error = true;

        if(!error){
            resolve();
        }else{
            reject('Something went wrong');
        }
    }, 2000);        
    });
}

//createPost({title: 'Post Three', body:'The streigth in loss'})
//.then(getPosts)
//.catch(err => console.log(err))

const promise1 = Promise.resolve("Hello World");
const promise2 = 10;
const promise3 = new Promise((resolve, reject))
setTimeout(resolve)


Promise.all([promise1, promise2, promise3])
.then((value)=>console.log(value));