
setTimeout(function () {
    console.log(3);
}, 0);
  
Promise.resolve().then(function () {
    console.log(2);
});
  
console.log(1);