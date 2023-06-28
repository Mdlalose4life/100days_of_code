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


function createPost(post, callback){
    setTimeout(() => {
        posts.push(post);
        callback();
    }, 2000);
}
getPosts();
createPost({title:'Post Three', body:'The strength in a loss'}, getPosts);