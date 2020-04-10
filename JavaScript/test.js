k = [];
console.log(typeof(k))
console.log(Object.prototype.toString.call(k))
console.log(k instanceof Array)
console.log(k.constructor == Array) // 不靠谱，constructor 可以被修改
console.log(Array.isArray(k)) 