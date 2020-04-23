let [a, b, c] = [1, 2, 3]
let [, , d] = [4, 5, 6]
let [e, ...f] = [7, 8, 9]
// 只有 === undefined，默认值才会生效
let [g = 10, h = 11] = [undefined, null]
let [i = 12, j = i] = []

console.log(a, b, c, d, e, f)
console.log(g, h, i, j)

console.log([1][0])


function test () {
    this.a = 1
}

test.prototype.a = 2
test.prototype.b = 3

let t = new test()

console.log(t.a)
console.log(t.b)
console.log('b' in t, t.hasOwnProperty('b'))