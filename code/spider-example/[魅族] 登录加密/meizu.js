/**
 * Created by PFinal南丞.
 * @Author :PFinal南丞<lampxiezi@163.com>
 * @Date   :2023/5/18 17:00
 * @File    : meizu.js
 * @Software: PyCharm
 */

var cryPP = {};
cryPP.excutePP = function (r, e) {
    for (var n = "", t = 0; t < r.length; t++) {
        var o = e ^ r.charCodeAt(t);
        n += String.fromCharCode(o)
    }
    return encodeURIComponent(n)
};
cryPP.generateMix = function (r) {
    return Math.ceil(1e3 * Math.random())
};

let kk = cryPP.generateMix();
console.log(kk)

passsword = cryPP.excutePP("11123123", kk);
console.log(passsword)