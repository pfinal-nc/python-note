/**
 * Created by PFinal南丞.
 * @Author :PFinal南丞<lampxiezi@163.com>
 * @Date   :2023/8/8 10:54
 * @File    : get_lun.js.js
 * @Software: PyCharm
 */

const lunisolar = require('lunisolar')
const theGods = require('lunisolar/plugins/theGods')
const takeSound = require('lunisolar/plugins/takeSound')
lunisolar.extend(theGods)
lunisolar.extend(takeSound)
function get_lun(date, to = 2) {
    let date_info = ''
    if (to === 1) {
        date = lunisolar.fromLunar({
            year: lunisolar(date).year,
            month: lunisolar(date).month,
            day: lunisolar(date).day
        }).format('YYYY/MM/DD')
    }
    date_info += '\n==============================\n'
    date_info += '阳历: ' + date
    const d = lunisolar(date)
    date_info += '\n农历: ' + d.format('lY年 lM(lL)lD lH時')
    date_info += '\n八字: ' + d.format('cY cM cD cH')
    date_info += '\n节气: ' + d.solarTerm?.toString()
    date_info += '\n命理: ' + d.char8.year.takeSound
    date_info += '\n==============================\n'

    console.log(date_info)
    return date_info
}

get_lun('1990/09/07', 1)