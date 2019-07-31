from MysqlLet import MySQLet
if __name__ == "__main__":
    mysqlet = MySQLet(host = "127.0.0.1",user = "root", password= "root", database = "scrapy_ip")
    data = mysqlet.query_formatrs('SELECT `ip` FROM proxy_ip');
    print(data)