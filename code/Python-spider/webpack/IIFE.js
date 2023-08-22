/**
 * Created by PFinal南丞.
 * @Author :PFinal南丞<lampxiezi@163.com>
 * @Date   :2023/8/22 09:37
 * @File    : IIFE.js
 * @Software: PyCharm
 */
// IIFE 全称 Immediately-invoked Function Expressions，译为立即调用函数表达式，也称为自执行函数、立即执行函数、自执行匿名函数等，IIFE 是一种语法，这种模式本质上就是函数表达式（命名的或者匿名的）在创建后立即执行。当函数变成立即执行的函数表达式时，表达式中的变量不能从外部访问。IIFE 主要用来隔离作用域，避免污染

// 匿名函数前加上一元操作符 后面加上 ()

!function () {
    console.log("I AM IIFE")
}();

-function () {
    console.log("I am IIFE")
}();

+function () {
    console.log("i am IIFE")
}();

~function () {
    console.log("i am IIFE")
}();

// 匿名函数后面加上() 然后再用() 将整个括起来

(function () {
    console.log("i am IIFE1")
}());

// 先用 () 将匿名函数括起来 再在后面加上 ()
(function () {
    console.log("i am IIFE and IIFE2")
})();

// 使用 箭头函数表达式 先用 () 将箭头函数表达式括起来 在咋后面加上 ()
(() => {
    console.log("i am IIFE and IIFE2")
})();

// 使用匿名函数前面加上 void 关键字 后面加上 () void 指定要计算或运行一个表达式, 但是不返回值
void function () {
    console.log("I am IIFE and IIFE2")
}();

// 有时候 可能立即执行函数前加分号的情况 这是因为立即执行函数通常作为一个单独模块使用一般是没有问题, 但是还是建议在立即执行哈啊桉树或者后面加上分号,这样可以有效地与前面后者后面的代码进行隔离


;(function () {
    console.log("I am IIFE and IIFE2")
}());

;!function () {
    console.log("I am IIFE and IIFE21")
}();

//////////////////////////////// IIFE 参数传递 //////////////////////////////////

var text = "I am IIFE and IIFE";
(function (params) {
    console.log(params)
})(text);

var dict = {name: "Bob", age: "20"};

(function () {
    console.log(dict.name);
})(dict);

var list = [1, 2, 3, 4, 5];

(function () {
    let sum = 0;
    for (let i = 0; i < list.length; i++) {
        sum += list[i];
    }
    console.log(sum);
})(list);

