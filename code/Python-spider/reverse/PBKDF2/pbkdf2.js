let CryptoJS = require('crypto-js')

function pbkdf2Encrypt() {
    let text = 'I lov Python'
    let salt = '12345d'
    let encryptedData = CryptoJS.PBKDF2(text, salt, {keySize: 128 / 32, iterations: 10})
    return encryptedData.toString()
}

console.log(pbkdf2Encrypt()) // 22192e6ab76569b73bf0c3e20a9e03df

