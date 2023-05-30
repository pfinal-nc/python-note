const crypto = require('crypto')

function m(e) {
    return crypto.createHash("md5").update(e).digest()
}

function decode(t, o, n) {
    if (!t)
        return null;
    const a = Buffer.alloc(16, m(o))
        , r = Buffer.alloc(16, m(n))
        , i = crypto.createDecipheriv("aes-128-cbc", a, r);
    let s = i.update(t, "base64", "utf-8");
    return s += i.final("utf-8"),
        s
}

var k = "ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl"
var iv = 'ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4'

function run(encode_data) {
    return (decode(encode_data, k, iv))
}