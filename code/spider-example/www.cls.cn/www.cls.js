let u = function (e) {
    for (e += 9; e % 64 > 0; e += 1)
        ;
    return e
}
let s = function (e) {
    var t = 0;
    if (e <= 65536) return 65536;
    if (e < 16777216) for (t = 1; t < e; t <<= 1) ; else for (t = 16777216; t < e; t += 16777216) ;
    return t
}
let r = function (e, t, n) {
    "use asm";
    var r = new e.Int32Array(n);

    function o(e, t) {
        e = e | 0;
        t = t | 0;
        var n = 0
            , o = 0
            , i = 0
            , s = 0
            , a = 0
            , u = 0
            , c = 0
            , f = 0
            , p = 0
            , h = 0
            , l = 0
            , d = 0
            , y = 0
            , m = 0;
        i = r[t + 320 >> 2] | 0;
        a = r[t + 324 >> 2] | 0;
        c = r[t + 328 >> 2] | 0;
        p = r[t + 332 >> 2] | 0;
        l = r[t + 336 >> 2] | 0;
        for (n = 0; (n | 0) < (e | 0); n = n + 64 | 0) {
            s = i;
            u = a;
            f = c;
            h = p;
            d = l;
            for (o = 0; (o | 0) < 64; o = o + 4 | 0) {
                m = r[n + o >> 2] | 0;
                y = ((i << 5 | i >>> 27) + (a & c | ~a & p) | 0) + ((m + l | 0) + 1518500249 | 0) | 0;
                l = p;
                p = c;
                c = a << 30 | a >>> 2;
                a = i;
                i = y;
                r[e + o >> 2] = m
            }
            for (o = e + 64 | 0; (o | 0) < (e + 80 | 0); o = o + 4 | 0) {
                m = (r[o - 12 >> 2] ^ r[o - 32 >> 2] ^ r[o - 56 >> 2] ^ r[o - 64 >> 2]) << 1 | (r[o - 12 >> 2] ^ r[o - 32 >> 2] ^ r[o - 56 >> 2] ^ r[o - 64 >> 2]) >>> 31;
                y = ((i << 5 | i >>> 27) + (a & c | ~a & p) | 0) + ((m + l | 0) + 1518500249 | 0) | 0;
                l = p;
                p = c;
                c = a << 30 | a >>> 2;
                a = i;
                i = y;
                r[o >> 2] = m
            }
            for (o = e + 80 | 0; (o | 0) < (e + 160 | 0); o = o + 4 | 0) {
                m = (r[o - 12 >> 2] ^ r[o - 32 >> 2] ^ r[o - 56 >> 2] ^ r[o - 64 >> 2]) << 1 | (r[o - 12 >> 2] ^ r[o - 32 >> 2] ^ r[o - 56 >> 2] ^ r[o - 64 >> 2]) >>> 31;
                y = ((i << 5 | i >>> 27) + (a ^ c ^ p) | 0) + ((m + l | 0) + 1859775393 | 0) | 0;
                l = p;
                p = c;
                c = a << 30 | a >>> 2;
                a = i;
                i = y;
                r[o >> 2] = m
            }
            for (o = e + 160 | 0; (o | 0) < (e + 240 | 0); o = o + 4 | 0) {
                m = (r[o - 12 >> 2] ^ r[o - 32 >> 2] ^ r[o - 56 >> 2] ^ r[o - 64 >> 2]) << 1 | (r[o - 12 >> 2] ^ r[o - 32 >> 2] ^ r[o - 56 >> 2] ^ r[o - 64 >> 2]) >>> 31;
                y = ((i << 5 | i >>> 27) + (a & c | a & p | c & p) | 0) + ((m + l | 0) - 1894007588 | 0) | 0;
                l = p;
                p = c;
                c = a << 30 | a >>> 2;
                a = i;
                i = y;
                r[o >> 2] = m
            }
            for (o = e + 240 | 0; (o | 0) < (e + 320 | 0); o = o + 4 | 0) {
                m = (r[o - 12 >> 2] ^ r[o - 32 >> 2] ^ r[o - 56 >> 2] ^ r[o - 64 >> 2]) << 1 | (r[o - 12 >> 2] ^ r[o - 32 >> 2] ^ r[o - 56 >> 2] ^ r[o - 64 >> 2]) >>> 31;
                y = ((i << 5 | i >>> 27) + (a ^ c ^ p) | 0) + ((m + l | 0) - 899497514 | 0) | 0;
                l = p;
                p = c;
                c = a << 30 | a >>> 2;
                a = i;
                i = y;
                r[o >> 2] = m
            }
            i = i + s | 0;
            a = a + u | 0;
            c = c + f | 0;
            p = p + h | 0;
            l = l + d | 0
        }
        r[t + 320 >> 2] = i;
        r[t + 324 >> 2] = a;
        r[t + 328 >> 2] = c;
        r[t + 332 >> 2] = p;
        r[t + 336 >> 2] = l
    }

    return {
        hash: o
    }
}


_offset = 0,
    t = 65536,
    _maxChunkLen = t,
    _padMaxChunkLen = u(t),
    _heap = new ArrayBuffer(s(_padMaxChunkLen + 320 + 20)),
    _h32 = new Int32Array(_heap),
    _h8 = new Int8Array(_heap)
_core = new r({Int32Array: Int32Array}, {}, _heap)
let a = function (e, t, i, s, a, u) {
    if ("string" === typeof e)
        return function (e, t, n, r, o, i) {
            var s = void 0
                , a = i % 4
                , u = (o + a) % 4
                , c = o - u;
            switch (a) {
                case 0:
                    t[i] = e.charCodeAt(r + 3);
                case 1:
                    t[i + 1 - (a << 1) | 0] = e.charCodeAt(r + 2);
                case 2:
                    t[i + 2 - (a << 1) | 0] = e.charCodeAt(r + 1);
                case 3:
                    t[i + 3 - (a << 1) | 0] = e.charCodeAt(r)
            }
            if (!(o < u + (4 - a))) {
                for (s = 4 - a; s < c; s = s + 4 | 0)
                    n[i + s >> 2] = e.charCodeAt(r + s) << 24 | e.charCodeAt(r + s + 1) << 16 | e.charCodeAt(r + s + 2) << 8 | e.charCodeAt(r + s + 3);
                switch (u) {
                    case 3:
                        t[i + c + 1 | 0] = e.charCodeAt(r + c + 2);
                    case 2:
                        t[i + c + 2 | 0] = e.charCodeAt(r + c + 1);
                    case 1:
                        t[i + c + 3 | 0] = e.charCodeAt(r + c)
                }
            }
        }(e, t, i, s, a, u);
    if (e instanceof Array)
        return o(e, t, i, s, a, u);
    if (n && n.Buffer && n.Buffer.isBuffer(e))
        return o(e, t, i, s, a, u);
    if (e instanceof ArrayBuffer)
        return o(new Uint8Array(e), t, i, s, a, u);
    if (e.buffer instanceof ArrayBuffer)
        return o(new Uint8Array(e.buffer, e.byteOffset, e.byteLength), t, i, s, a, u);
    if (e instanceof Blob)
        return function (e, t, n, o, i, s) {
            var a = void 0
                , u = s % 4
                , c = (i + u) % 4
                , f = i - c
                , p = new Uint8Array(r.readAsArrayBuffer(e.slice(o, o + i)));
            switch (u) {
                case 0:
                    t[s] = p[3];
                case 1:
                    t[s + 1 - (u << 1) | 0] = p[2];
                case 2:
                    t[s + 2 - (u << 1) | 0] = p[1];
                case 3:
                    t[s + 3 - (u << 1) | 0] = p[0]
            }
            if (!(i < c + (4 - u))) {
                for (a = 4 - u; a < f; a = a + 4 | 0)
                    n[s + a >> 2 | 0] = p[a] << 24 | p[a + 1] << 16 | p[a + 2] << 8 | p[a + 3];
                switch (c) {
                    case 3:
                        t[s + f + 1 | 0] = p[f + 2];
                    case 2:
                        t[s + f + 2 | 0] = p[f + 1];
                    case 1:
                        t[s + f + 3 | 0] = p[f]
                }
            }
        }(e, t, i, s, a, u);
    throw new Error("Unsupported data type.")
}
let c = function (e, t) {
    var n = new Int32Array(e, t + 320, 5)
        , r = new Int32Array(5)
        , o = new DataView(r.buffer);
    return o.setInt32(0, n[0], !1),
        o.setInt32(4, n[1], !1),
        o.setInt32(8, n[2], !1),
        o.setInt32(12, n[3], !1),
        o.setInt32(16, n[4], !1),
        r
}
let _initState = function (e, t) {
    _offset = 0;
    var n = new Int32Array(e, t + 320, 5);
    n[0] = 1732584193,
        n[1] = -271733879,
        n[2] = -1732584194,
        n[3] = 271733878,
        n[4] = -1009589776
}
let _padChunk = function (e, t) {
    var n = u(e)
        , r = new Int32Array(_heap, 0, n >> 2);
    return function (e, t) {
        var n = new Uint8Array(e.buffer)
            , r = t % 4
            , o = t - r;
        switch (r) {
            case 0:
                n[o + 3] = 0;
            case 1:
                n[o + 2] = 0;
            case 2:
                n[o + 1] = 0;
            case 3:
                n[o + 0] = 0
        }
        for (var i = 1 + (t >> 2); i < e.length; i++)
            e[i] = 0
    }(r, e),
        function (e, t, n) {
            e[t >> 2] |= 128 << 24 - (t % 4 << 3),
                e[14 + (2 + (t >> 2) & -16)] = n / (1 << 29) | 0,
                e[15 + (2 + (t >> 2) & -16)] = n << 3
        }(r, e, t),
        n
}
let _write = function (e, t, n, r) {
    a(e, _h8, _h32, t, n, r || 0)
}

let _coreCall = function (e, t, n, r, o) {
    var i = n;
    _write(e, t, n),
    o && (i = _padChunk(n, r))
    _core.hash(i, _padMaxChunkLen)
};
let rawDigest = function (e) {
    var t = e.byteLength || e.length || e.size || 0;
    _initState(_heap, _padMaxChunkLen);
    var n = 0
        , r = _maxChunkLen;
    for (n = 0; t > n + r; n += r)
        _coreCall(e, n, r, t, !1);
    return _coreCall(e, n, t - n, t, !0),
        c(_heap, _padMaxChunkLen)
}
let i = function (e) {
    for (var n = new Array(256), r = 0; r < 256; r++)
        n[r] = (r < 16 ? "0" : "") + r.toString(16);
    for (var t = new Uint8Array(e), r = new Array(e.byteLength), o = 0; o < r.length; o++)
        r[o] = n[t[o]];
    return r.join("")

    // for (var t = new Uint8Array(e), r = new Array(e.byteLength), o = 0; o < r.length; o++) r[o] = n[t[o]];
    // return r.join("")
}
var mmnf = {
    utf8: {
        stringToBytes: function (e) {
            return mmnf.bin.stringToBytes(unescape(encodeURIComponent(e)))
        },
        bytesToString: function (e) {
            return decodeURIComponent(escape(mmnf.bin.bytesToString(e)))
        }
    },
    bin: {
        stringToBytes: function (e) {
            for (var t = [], n = 0; n < e.length; n++)
                t.push(255 & e.charCodeAt(n));
            return t
        },
        bytesToString: function (e) {
            for (var t = [], n = 0; n < e.length; n++)
                t.push(String.fromCharCode(e[n]));
            return t.join("")
        }
    }
};
var t = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    , nnn = {
    rotl: function (e, t) {
        return e << t | e >>> 32 - t
    },
    rotr: function (e, t) {
        return e << 32 - t | e >>> t
    },
    endian: function (e) {
        if (e.constructor == Number)
            return 16711935 & nnn.rotl(e, 8) | 4278255360 & nnn.rotl(e, 24);
        for (var t = 0; t < e.length; t++)
            e[t] = nnn.endian(e[t]);
        return e
    },
    randomBytes: function (e) {
        for (var t = []; e > 0; e--)
            t.push(Math.floor(256 * Math.random()));
        return t
    },
    bytesToWords: function (e) {
        for (var t = [], n = 0, r = 0; n < e.length; n++,
            r += 8)
            t[r >>> 5] |= e[n] << 24 - r % 32;
        return t
    },
    wordsToBytes: function (e) {
        for (var t = [], n = 0; n < 32 * e.length; n += 8)
            t.push(e[n >>> 5] >>> 24 - n % 32 & 255);
        return t
    },
    bytesToHex: function (e) {
        for (var t = [], n = 0; n < e.length; n++)
            t.push((e[n] >>> 4).toString(16)),
                t.push((15 & e[n]).toString(16));
        return t.join("")
    },
    hexToBytes: function (e) {
        for (var t = [], n = 0; n < e.length; n += 2)
            t.push(parseInt(e.substr(n, 2), 16));
        return t
    },
    bytesToBase64: function (e) {
        for (var n = [], r = 0; r < e.length; r += 3)
            for (var o = e[r] << 16 | e[r + 1] << 8 | e[r + 2], i = 0; i < 4; i++)
                8 * r + 6 * i <= 8 * e.length ? n.push(t.charAt(o >>> 6 * (3 - i) & 63)) : n.push("=");
        return n.join("")
    },
    base64ToBytes: function (e) {
        e = e.replace(/[^A-Z0-9+\/]/gi, "");
        for (var n = [], r = 0, o = 0; r < e.length; o = ++r % 4)
            0 != o && n.push((t.indexOf(e.charAt(r - 1)) & Math.pow(2, -2 * o + 8) - 1) << 2 * o | t.indexOf(e.charAt(r)) >>> 6 - 2 * o);
        return n
    }
}

let s2 = function (e, t, n) {
    var t = nnn,
        r = mmnf['utf8'],

        o = function (e) {
            return null != e && (n(e) || function (e) {
                return "function" === typeof e.readFloatLE && "function" === typeof e.slice && n(e.slice(0, 0))
            }(e) || !!e._isBuffer)
        },
        i = mmnf['bin'],
        s = function (e, n) {
            e.constructor == String ? e = n && "binary" === n.encoding ? i.stringToBytes(e) : r.stringToBytes(e) : o(e) ? e = Array.prototype.slice.call(e, 0) : Array.isArray(e) || (e = e.toString());
            for (var a = t.bytesToWords(e), u = 8 * e.length, c = 1732584193, f = -271733879, p = -1732584194, h = 271733878, l = 0; l < a.length; l++)
                a[l] = 16711935 & (a[l] << 8 | a[l] >>> 24) | 4278255360 & (a[l] << 24 | a[l] >>> 8);
            a[u >>> 5] |= 128 << u % 32,
                a[14 + (u + 64 >>> 9 << 4)] = u;
            var d = s._ff
                , y = s._gg
                , v = s._hh
                , g = s._ii;
            for (l = 0; l < a.length; l += 16) {
                var m = c
                    , w = f
                    , x = p
                    , b = h;
                c = d(c, f, p, h, a[l + 0], 7, -680876936),
                    h = d(h, c, f, p, a[l + 1], 12, -389564586),
                    p = d(p, h, c, f, a[l + 2], 17, 606105819),
                    f = d(f, p, h, c, a[l + 3], 22, -1044525330),
                    c = d(c, f, p, h, a[l + 4], 7, -176418897),
                    h = d(h, c, f, p, a[l + 5], 12, 1200080426),
                    p = d(p, h, c, f, a[l + 6], 17, -1473231341),
                    f = d(f, p, h, c, a[l + 7], 22, -45705983),
                    c = d(c, f, p, h, a[l + 8], 7, 1770035416),
                    h = d(h, c, f, p, a[l + 9], 12, -1958414417),
                    p = d(p, h, c, f, a[l + 10], 17, -42063),
                    f = d(f, p, h, c, a[l + 11], 22, -1990404162),
                    c = d(c, f, p, h, a[l + 12], 7, 1804603682),
                    h = d(h, c, f, p, a[l + 13], 12, -40341101),
                    p = d(p, h, c, f, a[l + 14], 17, -1502002290),
                    c = y(c, f = d(f, p, h, c, a[l + 15], 22, 1236535329), p, h, a[l + 1], 5, -165796510),
                    h = y(h, c, f, p, a[l + 6], 9, -1069501632),
                    p = y(p, h, c, f, a[l + 11], 14, 643717713),
                    f = y(f, p, h, c, a[l + 0], 20, -373897302),
                    c = y(c, f, p, h, a[l + 5], 5, -701558691),
                    h = y(h, c, f, p, a[l + 10], 9, 38016083),
                    p = y(p, h, c, f, a[l + 15], 14, -660478335),
                    f = y(f, p, h, c, a[l + 4], 20, -405537848),
                    c = y(c, f, p, h, a[l + 9], 5, 568446438),
                    h = y(h, c, f, p, a[l + 14], 9, -1019803690),
                    p = y(p, h, c, f, a[l + 3], 14, -187363961),
                    f = y(f, p, h, c, a[l + 8], 20, 1163531501),
                    c = y(c, f, p, h, a[l + 13], 5, -1444681467),
                    h = y(h, c, f, p, a[l + 2], 9, -51403784),
                    p = y(p, h, c, f, a[l + 7], 14, 1735328473),
                    c = v(c, f = y(f, p, h, c, a[l + 12], 20, -1926607734), p, h, a[l + 5], 4, -378558),
                    h = v(h, c, f, p, a[l + 8], 11, -2022574463),
                    p = v(p, h, c, f, a[l + 11], 16, 1839030562),
                    f = v(f, p, h, c, a[l + 14], 23, -35309556),
                    c = v(c, f, p, h, a[l + 1], 4, -1530992060),
                    h = v(h, c, f, p, a[l + 4], 11, 1272893353),
                    p = v(p, h, c, f, a[l + 7], 16, -155497632),
                    f = v(f, p, h, c, a[l + 10], 23, -1094730640),
                    c = v(c, f, p, h, a[l + 13], 4, 681279174),
                    h = v(h, c, f, p, a[l + 0], 11, -358537222),
                    p = v(p, h, c, f, a[l + 3], 16, -722521979),
                    f = v(f, p, h, c, a[l + 6], 23, 76029189),
                    c = v(c, f, p, h, a[l + 9], 4, -640364487),
                    h = v(h, c, f, p, a[l + 12], 11, -421815835),
                    p = v(p, h, c, f, a[l + 15], 16, 530742520),
                    c = g(c, f = v(f, p, h, c, a[l + 2], 23, -995338651), p, h, a[l + 0], 6, -198630844),
                    h = g(h, c, f, p, a[l + 7], 10, 1126891415),
                    p = g(p, h, c, f, a[l + 14], 15, -1416354905),
                    f = g(f, p, h, c, a[l + 5], 21, -57434055),
                    c = g(c, f, p, h, a[l + 12], 6, 1700485571),
                    h = g(h, c, f, p, a[l + 3], 10, -1894986606),
                    p = g(p, h, c, f, a[l + 10], 15, -1051523),
                    f = g(f, p, h, c, a[l + 1], 21, -2054922799),
                    c = g(c, f, p, h, a[l + 8], 6, 1873313359),
                    h = g(h, c, f, p, a[l + 15], 10, -30611744),
                    p = g(p, h, c, f, a[l + 6], 15, -1560198380),
                    f = g(f, p, h, c, a[l + 13], 21, 1309151649),
                    c = g(c, f, p, h, a[l + 4], 6, -145523070),
                    h = g(h, c, f, p, a[l + 11], 10, -1120210379),
                    p = g(p, h, c, f, a[l + 2], 15, 718787259),
                    f = g(f, p, h, c, a[l + 9], 21, -343485551),
                    c = c + m >>> 0,
                    f = f + w >>> 0,
                    p = p + x >>> 0,
                    h = h + b >>> 0
            }
            return t.endian([c, f, p, h])
        };
    s._ff = function (e, t, n, r, o, i, s) {
        var a = e + (t & n | ~t & r) + (o >>> 0) + s;
        return (a << i | a >>> 32 - i) + t
    }
        ,
        s._gg = function (e, t, n, r, o, i, s) {
            var a = e + (t & r | n & ~r) + (o >>> 0) + s;
            return (a << i | a >>> 32 - i) + t
        }
        ,
        s._hh = function (e, t, n, r, o, i, s) {
            var a = e + (t ^ n ^ r) + (o >>> 0) + s;
            return (a << i | a >>> 32 - i) + t
        }
        ,
        s._ii = function (e, t, n, r, o, i, s) {
            var a = e + (n ^ (t | ~r)) + (o >>> 0) + s;
            return (a << i | a >>> 32 - i) + t
        }
        ,
        s._blocksize = 16,
        s._digestsize = 16,
        result = function (e, n) {

            // var r = t.wordsToBytes([-1089522060, 1658375536, -1854167574, -1283114034]);
            var r = t.wordsToBytes(s(e, n));

            return n && n.asBytes ? r : n && n.asString ? i.bytesToString(r) : t.bytesToHex(r)
        }
    return result(e)
}

function getEncryptedSign(t) {
    sign1 = i(rawDigest(t).buffer)
    console.log(sign1)
    sign2 = s2(sign1)
    console.log(sign2)
    return sign2
}

getEncryptedSign("app=CailianpressWeb&id=1000&last_time=&os=web&rn=20&sv=7.7.5")

// function(e,t,a){a("GcxT"),e.exports=a("nOHt")}