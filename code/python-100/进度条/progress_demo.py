# -*- coding: utf-8 -*-
# @Time    : 2023/7/13 09:21
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : progress_demo.py
# @Software: PyCharm


# max： 进度条最大进度
# fill：进度条填充的字符
# suffix：百分比的样式

# bar = Bar('Processing', max=100, fill='#', suffix='%(percent)d%%')
# for i in range(100):
#     time.sleep(0.1)
#     bar.next()
# bar.finish()

import time
import progressbar

widgets = [
    'Loading: ',
    '[', progressbar.AnimatedMarker(), ']',
    ' ',
    progressbar.Timer()
]
bar = progressbar.ProgressBar(
    widgets=widgets, max_value=progressbar.UnknownLength)

for i in range(100):
    time.sleep(0.5)
    bar.update(i)