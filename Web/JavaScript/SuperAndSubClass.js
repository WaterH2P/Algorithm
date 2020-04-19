function Animal(name){
    this.name = name || 'Animal';
    this.sleep = () => { console.log(this.name + ' 正在睡觉！'); }
  }
  Animal.prototype.eat = (food) => { console.log(this.name + ' 正在吃：' + food); }
  
  function Cat(name){
    Animal.call(this);
    this.name = name || 'Tom';
  }
  (() => {
    let tmp = object(Animal.prototype);
    tmp.constructor = Cat;
    Cat.prototype = tmp;
  })
  
  // Test Code
  var cat = new Cat();
  console.log(cat.name);
  console.log(cat.sleep());
  console.log(cat instanceof Animal); // false
  console.log(cat instanceof Cat); //true