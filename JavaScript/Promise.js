let promise = new Promise(function(resolve, reject){
    // resolve('123');
    reject('123');
    // throw new Error('hhhh');
})

promise.then(msg => console.log(`hello`), 
             msg => console.log(`eee`))
        .then(msg => console.log(`hello`), 
             msg => console.log(`eee`));