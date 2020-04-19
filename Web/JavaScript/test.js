// k = [];
// console.log(typeof(k))
// console.log(Object.prototype.toString.call(k))
// console.log(k instanceof Array)
// console.log(k.constructor == Array) // 不靠谱，constructor 可以被修改
// console.log(Array.isArray(k)) 

k = [1, 2, 3, 4]
console.log(k.join(' '))

k = {
    test1: 1,
    test2: 2
}

a = 1
let {test1, test2} = k
s = {...k, test1, a}
console.log(test1)
console.log(s)