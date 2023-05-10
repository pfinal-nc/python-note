function oQ0OQ(Q0o0, o0OQ) {
    return Q0o0 < o0OQ;
}

function O000O(Q0o0, o0OQ) {
    return Q0o0 >> o0OQ;
}

function Qo0oo(Q0o0, o0OQ) {
    return Q0o0 | o0OQ;
}

function OOO0Q(Q0o0, o0OQ) {
    return Q0o0 << o0OQ;
}

function OooQo(Q0o0, o0OQ) {
    return Q0o0 & o0OQ;
}

function Oo0OO(Q0o0, o0OQ) {
    return Q0o0 + o0OQ;
}

var oQoo0 = {};
oQoo0["_keyStr"] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=",
oQoo0["encode"] = function QQQ0(Q0o0) {
        var o0OQ = 62;
        while (o0OQ) {
            switch (o0OQ) {
                case 116 + 13 - 65: {}
                case 118 + 8 - 63: {}
                case 94 + 8 - 40: {}
                case 122 + 6 - 63: {}
            }
        }
    };
oQoo0["_utf8_encode"] = function oOQ0(Q0o0) {}

function OOoO0() {
    var tokens = "e0ia+fB5zvGuTjFDgcKahQwg2UEH8b0k7EK/Ukt4KwzyCbpm11jjy8Au64MC6s7HvLRacUxd7ka4AdDidJmYAA==";
    var version = "+X+3JWoUVBc12xtmgMpwzjAone3cp6/4QuFj7oWKNk+C4tqy4un/e29cODlhRmDy";
    var Oo0O0 = {};
    Oo0O0["blackBox"] = {};
    Oo0O0["blackBox"]["v"] = version;
    Oo0O0["blackBox"]["os"] = "web";
    Oo0O0["blackBox"]["it"] = parseInt(Math.random() * 100000);
    Oo0O0["blackBox"]["t"] = tokens;
    return oQoo0["encode"](JSON.stringify(Oo0O0["blackBox"]));
}

// 测试样例
console.log(OOoO0())