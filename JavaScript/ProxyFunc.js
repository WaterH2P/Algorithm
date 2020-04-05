let validator = {
    set: (obj, prop, value) => {
        if (prop == 'age') {
            if (!Number.isInteger(value)) {
                throw new TypeError('The age is not an integer');
            }
            if (value > 160) {
                throw new RangeError('The age seems invalid');
            }
        }
        obj[prop] = value;
    }
}

let person = new Proxy({}, validator);

person.age = 20;
console.log(person.age)
person.age = 200;
console.log(person.age)