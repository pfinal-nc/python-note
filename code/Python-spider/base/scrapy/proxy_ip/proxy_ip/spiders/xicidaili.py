# -*- coding: utf-8 -*-
import scrapy

from scrapy.http import Request
from proxy_ip.items import ProxyIpItem
from proxy_ip.util import DatetimeUtil


class ProxyIp(scrapy.Spider):
    name = 'proxy_ip'
    allowed_domains = ['www.xicidaili.com']
    # start_urls = ['http://www.xicidaili.com/nn/1']

    def start_requests(self):
        start_url = 'http://www.xicidaili.com/nn/'

        for i in range(1, 6):
            url = start_url + str(i)
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        ip_table = response.xpath('//table[@id="ip_list"]/tr')
        proxy_ip = ProxyIpItem()

        for tr in ip_table[1:]:
            # 提取内容列表
            country = tr.xpath('td[1]/img/@alt')
            ip = tr.xpath('td[2]/text()')
            port = tr.xpath('td[3]/text()')
            server_location = tr.xpath('td[4]/a/text()')
            is_anonymous = tr.xpath('td[5]/text()')
            protocol_type = tr.xpath('td[6]/text()')
            speed = tr.xpath('td[7]/div[1]/@title')
            connect_time = tr.xpath('td[8]/div[1]/@title')
            survival_time = tr.xpath('td[9]/text()')
            validate_time = tr.xpath('td[10]/text()')

            # 提取目标内容
            proxy_ip['country'] = country.extract()[0].upper() if country else ''
            proxy_ip['ip'] = ip.extract()[0] if ip else ''
            proxy_ip['port'] = port.extract()[0] if port else ''
            proxy_ip['server_location'] = server_location.extract()[0] if server_location else ''
            proxy_ip['is_anonymous'] = is_anonymous.extract()[0] if is_anonymous else ''
            proxy_ip['protocol_type'] = protocol_type.extract()[0] if type else ''
            proxy_ip['speed'] = speed.extract()[0] if speed else ''
            proxy_ip['connect_time'] = connect_time.extract()[0] if connect_time else ''
            proxy_ip['survival_time'] = survival_time.extract()[0] if survival_time else ''
            proxy_ip['validate_time'] = '20' + validate_time.extract()[0] + ':00' if validate_time else ''
            proxy_ip['source'] = 'www.xicidaili.com'
            proxy_ip['create_time'] = DatetimeUtil.get_current_localtime()

            yield proxy_ip
