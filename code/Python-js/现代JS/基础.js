// "use strict"
//console.log("hello");
//[1, 2].forEach(console.log);

// use strict  这个指令整个脚本文件将以现在模式进行工作  注意一定需要放到 最上面  也可以如下使用:

(function(){
    'use strict'
})()

/**
 * 现代 JavaScript 支持 “class” 和 “module” —— 高级语言结构（本教程后续章节会讲到），它们会自动启用 use strict。因此，如果我们使用它们，则无需添加 "use strict" 指令。

因此，目前我们欢迎将 "use strict"; 写在脚本的顶部。稍后，当你的代码全都写在了 class 和 module 中时，你则可以将 "use strict"; 这行代码省略掉。

目前，我们已经基本了解了 use strict。

在接下来的章节中，当我们学习语言功能时，我们会看到严格模式与旧的模式之间的差异。幸运的是，差异其实没有那么多。并且，这些差异实际上提升了我们的编程体验。

本教程的所有例子都默认采用严格模式，除非特别指定（非常少）。
 */

/**
 * 变量 是数据中 命名存储,可以使用变量来保存商品, 访客和其他信息,在javascrript 中创建一个变量.我们需要用到let关键字
 */


let messages;

messages ='Hello'; // 将字符串 Hello 保存名为  message 的变量中

console.log(messages)


// 数据类型 object 和 symbol 类型
// object 类型是一个特殊的类型, 其他所有的数据类型都被称为原始类型, 因为他们的值只包含一个单独的内容(字符串,数字或者其他)。相反, object 则用于存储数据集合和 更 复杂 的实体
// symbol 类型用于创建对象的唯一标识符,symbol类型是为了完整性





/**
 * typeof 运算符
 * typeof 运算符返回 参数的类型,
 * 
 */

console.log(typeof undefined)// "undefined"
console.log(typeof 0) // "number"
console.log(typeof 10n)  // "bigint"
console.log(typeof true) //  "boolean"
console.log(typeof "foo") // "string"
console.log(typeof Symbol("id")) // "symbol"
console.log(typeof Math)  // "object" (1)
console.log(typeof null)  // "object" (2)
console.log(typeof alert) //  "function" 

/**
    number 用于任何类型的数字：整数或浮点数，在 ±(253-1) 范围内的整数。
    bigint 用于任意长度的整数。
    string 用于字符串：一个字符串可以包含 0 个或多个字符，所以没有单独的单字符类型。
    boolean 用于 true 和 false。
    null 用于未知的值 —— 只有一个 null 值的独立类型。
    undefined 用于未定义的值 —— 只有一个 undefined 值的独立类型。
    symbol 用于唯一的标识符。
    object 用于更复杂的数据结构。
 */


// 交互 alert ,prompt ,confirm
// alert('hello js')
//result = prompt(title,[default])
// let age = prompt('how old  are you ',100)
// console.log(age)

//  类型转换
let str = "123"
console.log(typeof str)
let num = Number(str)
console.log(num)

// 函数箭头

let sum = (a,b) => a+b;
console.log(sum(1,2))

let double =  n=> n*2
console.log(double(2))

// 箭头函数可以像函数表达式一样使用
let age = 20
let wc= (age<18)?
    ()=>console.log('打野的'):
    ()=>console.log('辅助的');
wc();

// 多行的箭头函数

let sum1 = (a,b)=> { // 花括号表示一个多行函数 
    let result = a + b; 
    return result
};
console.log(sum1(2,3))


// ##################
// 对象  
let user = new Object(); //  构造 函数的语法
let user1 = {} // "字面量 "的语法

//  文本 属性

let  user2 = {
    name:"pfinal", // 键 "name"值  "pfinal"
    age: 30        // 键 "age"值 30 
}

// 属性有键 (或者也可以叫做名字或标识符), 位于冒号, ":"的前面, 只在毛好的右边.
// 在 user  对象中, 有两个属性:
// 1.第一个的键是 "name" 值是 "pfinal"

delete user2.age
console.log(user2)
/**
 * 
    属性的键必须是字符串或者 symbol（通常是字符串）。
    值可以是任何类型。
    可以用下面的方法访问属性：

    点符号: obj.property。
    方括号 obj["property"]，方括号允许从变量中获取键，例如 obj[varWithKey]。
    其他操作：

    删除属性：delete obj.prop。
    检查是否存在给定键的属性："key" in obj。
    遍历对象：for(let key in obj) 循环。
 */

    // Symbol 类型

    //  symbol 值表示唯一的标识符
    let id = Symbol("id"); //id 是描述为id的symbol

    let  id1 = Symbol("id");
    console.log(id== id1)  //false

    // 隐藏属性
    //  symbol 允许我们创建对象的隐藏属性, 任何的其他部分不能意外访问或重写这些属性 
    let  user3  = {
        name:"pfinal"
    }

    let uid = Symbol("uid")
    user3[uid] = 1;
    console.log(user3[uid])

    //  对象中使用 symbol

    let  user4 = {
        [uid]:4,
        name:"nn"
    }

    console.log(user4)

    //  symbol 在for in 中会被跳过
     
    let user5 = {
        [id]:"123",
        name:"pfinal",
        age:20
    }

    for (let key in user5) console.log(key,user5[key])

    // 全局  symbol

    let cid = Symbol.for("cid");// 如果 symbol 不存在 则 创建 
    //再次读取
    let cidAgain  = Symbol.for("cid")

    // 比较是否是同一个  
    console.log(cid===cidAgain) //true


    let globalSymbol = Symbol.for("name");
    let localSymbol = Symbol("name");

    console.log( Symbol.keyFor(globalSymbol) ); // name，全局 symbol
    console.log( Symbol.keyFor(localSymbol) ); // undefined，非全局
    console.log( localSymbol.description ); // name