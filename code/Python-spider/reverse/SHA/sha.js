let CryptoJS = require('crypto-js')

function SHA1Encrypt() {
        var text = "I love python!"
        return CryptoJS.SHA1(text).toString();
}

console.log(SHA1Encrypt())  // 23c02b203bd2e2ca19da911f1d270a06d86719fb


