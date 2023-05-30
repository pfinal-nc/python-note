// 引用 crypto-js 加密模块
var CryptoJS = require('crypto-js')

function getEncryptedParams() {
    t = new Date().getTime()
    sign = `client=fanyideskweb&mysticTime=${t}&product=webfanyi&key=fsdsogkndfokasodnaso`
    console.log(sign)
    var sign = CryptoJS.MD5(sign).toString()
    return {sign: sign, t: t}
}

// var ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
// var data = "测试"
// console.log(getEncryptedParams());


function getDecryptedResult(encryptedData) {

}
t = "Z21kD9ZK1ke6ugku2ccWu4n6eLnvoDT0YgGi0y3g-v0B9sYqg8L9D6UERNozYOHqiVjnOHNpHCXi1IrNyOiprGMb6MvP8o-xDLdvl_Q4B9YXGInmaRUGbrXVrHYEiSXh7kuRINeWJSe2BMp5dJx-b9b1EJvN5-9bxQ3eDwkO73ZWZBbLo88b0Rak93XMVH3vynNHDLlJWcGgFFPIFBD3AiXQNbslYAo1243hpimvqhvgGsJzVP-yU30FsZE63ij1WGF9RF2y9cZ9hqdO6HfoTq5012nDMcrYZnuDFxWZ1ITZ6yO_6y45u2WS1eHVV25aabU0Q86zx4oqYHu1SQuMVSj03xxKblRq7bztecaDoj0tdFe667lRYmaT_kr3Ig5oVa-CNLP33MrsKS1-wnZzVZMobCD8UQkpAYD7hwLWQSta5glhGf8f7EV_gTy0b_w28i-IGcW04XLjLUk3FlaYibrk1T0qwJ4cChMFhZ8V8BBnRHxequgM6fzvt0TsFxVR8Zvd_eD-PR6uGfrl6vWkMeWgosYWZrbRxB81FKgyYEm-Z42hWmxFVByelbhIzHj6D44oYlrGnTOx9ABaPl61EvUgrNAgB7G4kJ613fM7rUDLoDjdZf8KnyilKh1eHtc1GXxMrHJDxu29zc-rEwAIZ2gnysRt76EN0o8vkeP3XaEhVmV0XHkwntEetBDRJ4rPOzbL9hAfOwmaAmXDFzibhHrV6nelMeOSLkKzxOjs5UVPecPhSne8cz9V-I5UikVTr_AvDjQ74KQOdPeLopfHomCE6WV3iV6_3KoiHOGcEVssvfRKvfmss0QPPgUYDoBnpPfhNx6NgAh5lDTf9-ksT_XfVJwHwy5uzYsx057Sqq2rbxqbJqS5L4dtsY1K_GojNtkj_wT2lZXDA0Vgili9a-kKb5DHSAMyOGsuVbHaqnwaE7SqdTUeVAPLCmm2cdLucVVklASmfYnBrQy2PdjNBmBO1rMuP2qmx7WI2hqHUxxz3_w51S00Iy4RuI_-w24vsxDtfoJ-E7--GyWHZi8OlWYtLPebOUgtYH1RWasPr6QknNqdnxHll4qRBZFqOBqSkxXV8j7ZANZC9ikDYMv_Wb3mYm1DIYxSUbJe3SuLoQvv-IVgthu0R_tXSwfGzDs-eYPVq0Wnk9BoX9uEqqC5Ro6IKhSvbypTw5_aJN8t3rutu1ulwnFg96Lv7rJ_8NJOGbVC3-OctZgdtLaRHywHv2F0wXCLmEnqdAISo8OZD1Z1D1LdpDoWgf6XbrmS37YCeXaAxBZtIZ6myiOG2MbegEv5eSI3kJOa1ZhOShcFvcQYiWIgzVVMXxrU0RKQxuONUvpJl6DQSdlApii7UjUFwC76opC_P-3qy98dlby8NyzekxBlGNQWQCHW0Y9R8EKU"
console.log(getDecryptedResult(t))