let promise = new Promise(function(resolve, reject){
    resolve('123');   
})

promise.then(msg => console.log(msg));