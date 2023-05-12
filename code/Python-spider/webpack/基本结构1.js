/**
 * Created by PFinal南丞.
 * @Author :PFinal南丞<lampxiezi@163.com>
 * @Date   :2023/5/12 13:26
 * @File    : 基本结构1.js
 * @Software: PyCharm
 */

!function (e) {
    var t = {}

    function d(n) {
        if (t[n])
            return t[n].exports;
        var r = t[n] = {
            i: n,
            l: !1,
            exports: {}
        }
        return e[n].call(r.exports, r, r.exports, d),
            r.l = !0, r.exports
    }
    d(0)
}([
    function () {
        console.log("我是模块1")
    },
    function () {
        console.log("我是模块2")
    }
])