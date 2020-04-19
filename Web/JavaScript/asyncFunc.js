async function asyncFn(){
    return '我后执行';
}
asyncFn().then((result)=>{
    console.log(result);
})

console.log('我先执行');

async function asyncError(){
    throw new Error('new error');
}

asyncError()
.then((success)=>{
    console.log('success');
}, (error)=>{
    console.log('then error', error);
}).catch((error)=>{
    console.log('catch error', error);
})