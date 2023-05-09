let CryptoJS = require('crypto-js')

function HMACEncrypt() {
    let text = "I love python!"
    let key = "secret"
    return CryptoJS.HmacMD5(text, key).toString();
}

console.log(HMACEncrypt())