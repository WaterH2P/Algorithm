let baa = {
    a: 1,
    b: 2
}

let bab = {
    a: 3,
    b: 3,
    c: 3
}

bab = {...bab, ...baa}

console.log(bab)

function test (obj) {
    for (property in obj) {
        obj[property] = 'a'
    }
    console.log(obj)
}

test({...bab})
console.log(bab)