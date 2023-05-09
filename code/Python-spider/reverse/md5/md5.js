let CryptoJS = require('crypto-js')

function MD5Test() {
    let text = 'hello world'
    return new CryptoJS.MD5(text).toString()
}

console.log(MD5Test()) // 输出5eb63bbbe01eeed093cb22bb8f5acdc3
