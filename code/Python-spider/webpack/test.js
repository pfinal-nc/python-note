/**
 * Created by PFinal南丞.
 * @Author :PFinal南丞<lampxiezi@163.com>
 * @Date   :2023/5/9 14:26
 * @File    : test.js
 * @Software: PyCharm
 */
//  正常 JS 写法=================================================================
// function a() {
//     console.log("a")
// }
//
// function b() {
//     console.log("b")
// }
//
// function c() {
//     console.log("c")
// }
//
// a()
// b()
// c()

!function (i) {
    function n(t) {
        return i[t].call(a, b, c, d)
    }
}([
    function (t, e) {
    },
    function (t, e, n) {
    },
    function (t, e, r) {
    },
    function (t, e, o) {
    }
])

// 这种写法相当于进行了模块化编程，我们称其为 webpack，上面的示例看起来比较费劲，简单优化一下：

!function (allModule) {
    function useModule(whichModule) {
        allModule[whichModule].call(null, 'hello world!');
    }

    useModule(0)
}([
    function module0(param) {
        console.log("module0: " + param)
    },
    function module1(param) {
        console.log("module1: " + param)
    },
    function module2(param) {
        console.log("module2: " + param)
    },
])

/**
 * 运行以上代码，会输出 module0: hello world!，相信通过浅显易懂的变量名和函数名，应该就可以看懂大致含义了，调用 useModule(0)，从所有函数里选择第一个，将 hello world! 传递给 module0 并输出。
 */

// 在 ECMAScript 中有两个最常用的创建 函数对象 的方法,即使使用函数或者函数表达式,ECMAScript 规范明确了一点  既函数声明必须始终带有一个标识符

// ===================
test("hello")

function test(msg) {
    console.log(msg)
}

var test = function (arg) {
    console.log(arg)
}

test("请道友升仙")

// =========================
/**
 *   IIFE 称为自执行函数、立即执行函数、自执行匿名函数等，IIFE 是一种语法，这种模式本质上就是函数表达式（命名的或者匿名的）在创建后立即执行。当函数变成立即执行的函数表达式时，表达式中的变量不能从外部访问。IIFE 主要用来隔离作用域，避免污染。
 */

// 1. 匿名 函数前面加上一元操作符 后面加上()

!function () {
    console.log("I M 格鲁特")
}();

-function () {
    console.log("道友你好")
}();

+function () {
    console.log("道可道")
}();

~function () {
    console.log("名可名")
}();

// 2.匿名函数后加上() 然后再用 () 将整个括起来

(function () {
    console.log("教书匠")
}());

// 3.先用() 将 匿名函数包括起来, 再在后面加上 ():
(function () {
    console.log("道德主义")
})();

// 4.使用箭头函数表达式, 先用() 将箭头函数表达式括起来 再在后面加上()
(() => {
    console.log("测试")
})()

// 5. 匿名函数前面加上 void 关键字 后面加上(), void 指定要计算或运行一个表达式 ，但是不返回值:

void function () {
    console.log("void 测试")
}()

// 6.立即执行函数前面后分号的情况

;(function () {
    console.log("测试啥")
}())
;!(function () {
    console.log("学习")
}())


// IIFE 参数传递 ===================================
// 1.将参数放在末尾的 () 里即可实现参数传递

let text = "我思故我在";
(function (params) {
    console.log(params)
}(text));

let dict = {name: "Bob", age: "20"};

(function () {
    console.log(dict.name);
})(dict);

let list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9];

(function () {
    let sum = 0;
    for (let i = 0; i < list.length; i++) {
        sum += list[i]
    }
    console.log(sum)
})(list)

// =================================================================
// Function.prototype.call() 都是比较常用的方法, 它们的作用一模一样 即改变函数中的this 指向, 它们的区别如下:

// call() 方法会立即执行这个函数 接受一个多个参数, 参数之间 用逗号隔开;
// apply() 方法会立即执行这个函数 接受一个包含多个参数的数组;
// bind() 方法不会立即执行这个函数 返回的是一个修改过后的函数, 便于稍后调用 接受的参数和 call() 一样

// call() 方法接受多个参数, 第一个参数 thisArg 指定了函数体内this 对象的指向,如果这个函数处于 非严格模式下, 制定为 null 或 undefined 时会自动替换为指向全局对象
// 在严格模式下，函数体内的 this 还是为 null。从第二个参数开始往后，每个参数被依次传入函数，基本语法如下：
// function.call(this,arg1,arg2,...)
// call
function testcall(a, b, c) {
    console.log(a + b + c)
}

testcall.call(null, 1, 2, 3)

function testcall2() {
    console.log(this.firstName + " " + this.lastName)
}

let data = {firstName: "John", lastName: "Doe"}
testcall2.call(data)

// apply() ===============================

// apply()  方法接受两个参数, 第一个参数 thisArg 与 call() 方法一致，第二个参数 为一个带下标的集合, 从 ECMAScript 第5版开始，这个集合可以为数组，也可以为类数组，apply() 方法把这个集合中的元素作为参数传递给被调用的函数，基本语法如下：
// function apply(thisArg,[arg1,arg2,....]) {}

function tests(a, b, c) {
    console.log(a + b + c)
}

tests.apply(null, [1, 2, 3])

function test_call() {
    console.log(this.firstName + " " + this.lastName)
}

test_call.apply(data)

// =================================================================

// bind()  方法和 call() 接受的参数是相同的, 只不过 bind() 返回的是一个函数,基本语法如下:
// function.bind(thisArgs,arg1,arg2,....)

function test(a, b, c) {
    console.log(a, b, c)
}

test.bind(null, 1, 2, 3)()

function test_bind() {
    console.log(this.firstName + " " + this.lastName)
}
test_bind.bind(data)()

