/**
 * Created by PFinal南丞.
 * @Author :PFinal南丞<lampxiezi@163.com>
 * @Date   :2023/5/12 13:31
 * @File    : 基本结构2.js
 * @Software: PyCharm
 */

!function(e){
    var t = {}
    function d(n) {
        if (t[n])
            return t[n].exports;
        var r = t[n] = {
            i:n,
            l:!1,
            exports: {}
        }
        return e[n].call(r.exports,r,r.exports,d),r.l = !0,r.exports
    }
    d('1x2y')
}({
    'qres':function(){
        console.log('我是模块1')
    },
    '1x2y':function(){
        console.log('我是模块2')
    }
})