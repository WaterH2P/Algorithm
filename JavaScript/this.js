
function Person() {
    // 构造函数 Person() 定义的 `this` 就是新实例对象自己
    this.age = 0;
    setInterval(function growUp() {
        // 在非严格模式下，growUp() 函数定义了其内部的 `this`
        // 为全局对象, 不同于构造函数Person()的定义的 `this`
        this.age++;
        console.log(this.age);
    }, 1000);

    // 利用箭头函数
    // 箭头函数则会捕获其所在上下文的  this 值，作为自己的 this 值
    setInterval(() => {
        this.age++;
        console.log(this.age);
    }, 1000);

    // 利用 bind 改变 this
    setInterval((function growUp() {
        this.age++;
        console.log(this.age);
    }).bind(this), 1000);
}
   
var p = new Person()