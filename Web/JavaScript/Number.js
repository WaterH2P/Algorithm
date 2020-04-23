// 二进制和八进制
console.log(0b111110111 === 503)
console.log(0o767 === 503)
console.log(parseInt('111110111', 2) === Number('0b111110111'))

console.log('\nNumber.isFinite')
console.log(Number.isFinite('1'))
console.log(Number.isFinite(NaN))
console.log(Number.isFinite(Infinity))
console.log(Number.isFinite(1))

console.log('\nNumber.isInteger')
console.log(Number.MIN_VALUE)
console.log(Number.isInteger(5E-324))
console.log(Number.isInteger(5E-325))   // 出现误判

console.log('\nNumber.EPSILON')
console.log(Number.EPSILON)             // JavaScript 能够表示的最小精度
console.log(Number.EPSILON.toFixed(20))

console.log('\nNumber.isSafeInteger')
console.log(Number.isSafeInteger(9007199254740993))
console.log(Number.isSafeInteger(9007199254740993 - 900))