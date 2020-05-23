// 蹦床函数（trampoline）可以将递归执行转为循环执行
function trampoline(f) {
    while (f && f instanceof Function) {
        f = f();
    }
    return f;
}

function sum(x, y) {
    if (y > 0) {
        return sum.bind(null, x + 1, y - 1);
    } else {
        return x;
    }
}

// 上面代码中，sum 函数的每次执行，都会返回自身的另一个版本。
// 现在，使用蹦床函数执行 sum，就不会发生调用栈溢出。
trampoline(sum(1, 100000))