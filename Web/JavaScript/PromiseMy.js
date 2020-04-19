class PromiseMy{
    constructor(process){
        this.status = 'pending';
        this.msg = '';
        process(this.resolve.bind(this), this.reject.bind(this));
        return this;
    }
    
    resolve(val){
        this.status = 'fulfilled';
        this.msg = val;
    }
    
    reject(err){
        this.status = 'rejected';
        this.msg = err;
    }
    
    then(resolve, reject){
        if (this.status === 'fulfilled'){
            resolve(this.msg);
        } else if (this.status === 'rejected') {
            reject(this.msg);
        }
    }
}

let test = new PromiseMy((resolve, reject) => {
    // resolve('123');
    reject('123');
}).then(
    (success) => console.log('success', success), 
    (failed) => console.log('failed', failed));