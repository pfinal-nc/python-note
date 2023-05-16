/**
 * Created by PFinal南丞.
 * @Author :PFinal南丞<lampxiezi@163.com>
 * @Date   :2023/5/16 16:17
 * @File    : youdao.js.js
 * @Software: PyCharm
 */

var n = {}
    , a = {}
    , c = o("1c46")
    , r = o.n(c)
    , i = {};
const {CancelToken: s} = i["a"];
let l;
const d = "fanyideskweb"
    , u = "webfanyi"
    , m = "client,mysticTime,product"
    , p = "1.0.0"
    , b = "web"
    , f = "fanyi.web";

function g(e) {
    return r.a.createHash("md5").update(e).digest()
}

function v(e) {
    return r.a.createHash("md5").update(e.toString()).digest("hex")
}

function h(e, t) {
    return v(`client=${d}&mysticTime=${e}&product=${u}&key=${t}`)
}

function get_sign() {

    console.log(e)
    sign = h(t, e)
}

get_sign()