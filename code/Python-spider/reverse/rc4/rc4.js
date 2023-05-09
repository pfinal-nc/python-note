/**
 * Created by PFinal南丞.
 * @Author :PFinal南丞<lampxiezi@163.com>
 * @Date   :2023/5/9 09:45
 * @File    : rc4.js
 * @Software: PyCharm
 */

let CryptoJS = require('crypto-js')

function RC4Encrypt() {
    return CryptoJS.RC4.encrypt(text, key).toString();
}

function RC4Decrypt() {
    return CryptoJS.RC4.decrypt(encryptedData, key).toString(CryptoJS.enc.Utf8);
}

var text = "I love Python!"
var key = "6f726c64f2c2057c"

var encryptedData = RC4Encrypt()
var decryptedData = RC4Decrypt()

console.log("加密字符串: ", encryptedData)
console.log("解密字符串: ", decryptedData)