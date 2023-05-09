// 引用 crypto-js 加密模块
var CryptoJS = require('crypto-js')

function base64Encode() {
    var srcs = CryptoJS.enc.Utf8.parse(text);
    var encodeData = CryptoJS.enc.Base64.stringify(srcs);
    return encodeData
}

function base64Decode() {
    var srcs = CryptoJS.enc.Base64.parse(encodeData);
    var decodeData = srcs.toString(CryptoJS.enc.Utf8);
    return decodeData
}

var text = "I love Python!"

var encodeData = base64Encode()
var decodeData = base64Decode()

console.log("Base64 编码: ", encodeData)
console.log("Base64 解码: ", decodeData)

// Base64 编码:  SSBsb3ZlIFB5dGhvbiE=
// Base64 解码:  I love Python!
