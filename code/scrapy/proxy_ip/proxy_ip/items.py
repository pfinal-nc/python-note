# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ProxyIpItem(scrapy.Item):
    country = scrapy.Field()
    ip = scrapy.Field()
    port = scrapy.Field( )
    server_location = scrapy.Field()
    is_anonymous = scrapy.Field()
    protocol_type = scrapy.Field()
    speed = scrapy.Field()
    connect_time = scrapy.Field()
    survival_time = scrapy.Field()
    validate_time = scrapy.Field()
    source = scrapy.Field()
    create_time = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """
            insert into proxy_ip(
              country, ip, port, server_location,
                is_anonymous, protocol_type, speed, connect_time,
                survival_time, validate_time, source, create_time
            )
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
        params = (
                    self["country"], self["ip"], self["port"], self["server_location"],
                    self["is_anonymous"], self["protocol_type"], self["speed"], self["speed"],
                    self["survival_time"], self["validate_time"], self["source"], self["create_time"]
                  )
        return insert_sql, params