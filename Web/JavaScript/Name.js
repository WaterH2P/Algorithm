console.log((new Function).name)

const headAndTail = (head, ...tail) => [head, ...tail];

console.log(headAndTail(1, 2, 3, 4, 5))
