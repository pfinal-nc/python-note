/**
 * Created by PFinal南丞.
 * @Author :PFinal南丞<lampxiezi@163.com>
 * @Date   :2023/5/9 15:58
 * @File    : 自执行.js.js
 * @Software: PyCharm
 */

//////////////////////////////// 自执行函数

!function (e) {
    console.log(e)
    var n = {
        t: "txt",
        exports: {},
        n: function () {
            console.log("function n ")
        }
    }
}("echo this")

!function (e) {
    console.log(e)
    var n = {
        t: "txt",
        exports: {},
        n: function () {
            console.log("function n ")
        }
    }
}(
    {
        "test": function () {
            console.log("test")
        }
    }
)

// 让 Vx 对象调用 _x 对象的  say() 方法

var Vx = {
    name: "一位不愿意透露姓名的热心网友",
    age: "18cm"
};

var _x = {
    name: "热心网友",
    age: "18mm",
    say: function () {
        console.log("name:" + this.name + " age:" + this.age)
    }
}

_x.say.call(Vx)

//////////////////////////////// load 加载器 //////////////////////////////////

// Webpack站点与普通站点的JS代码扣取是不一样的，因为Webpack站点的资源加载是围绕着加载器进行的，然后把静态资源当作模块传入调用，传入的模块就是参数，需要加载什么就运行什么模块。

// 简单加载器

// !function(e){
//     var t={}
//     function d(n){
//         if (t[n])
//             return t[n].exports;
//         console.log(n)
//         var r = t[n] = {
//             i:n,
//             l:!1,
//             exports:{}
//             };
//         return e[n].call(r.exports,r,r.exports,d),
//         r.l = !0;
//         r.exports
//     }
//
//     d(1)
//
// }(
//     [
//     function(){console.log("function1");console.log(this.r.i)},
//     function(){console.log("function2")}
//     ]
// );
//

// 加载器分析
// 将加载器拆分为两部分
