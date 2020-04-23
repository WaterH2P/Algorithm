let res = ''

console.log(/foo.bar/.test('foo\nbar'))
console.log(/foo[^]bar/.test('foo\nbar'))
console.log(/foo.bar/s.test('foo\nbar'))

// 先行断言
res = /\d+(?=%)/.exec('100% of US presidents have been male')
console.log(res[0])
res = /\d+(?!%)/.exec('that’s all 44 of them')
console.log(res[0])

// 后行断言
res = /(?<=\$)\d+/.exec('Benjamin Franklin is on the $100 bill')
console.log(res[0])
res = /(?<!\$)\d+/.exec('it’s is worth about €90')
console.log(res[0])

// 具名组匹配（暂不支持）
// res = /(?<year>\d{4})-(?<month>\d{2})-(?<day>\d{2})/.exec('2020-4-20')
// console.log(res.groups)


