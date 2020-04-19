var Singleton = (() => {
    let instance;
    var CreateSingleton = function(name) {
        this.name = name;
        if (instance) return instance;
        return instance = this;
    }
    CreateSingleton.prototype.getName = function() {
        return this.name;
    }
    return CreateSingleton;
})();

let a = new Singleton('a');
let b = new Singleton('b');
console.log(a.getName())
console.log(b.getName())
console.log(a === b)