let my = {
    money: 20
}
Object.defineProperty(my, 'money', {
    set: (number) => {
        console.log(`你存入 ${number} 元。`)
        money = number;
    },
    get: () => {
        console.log(`你有 ${money} 元。`)
        return money;
    }
})

my.money = 1000
console.log(my.money)