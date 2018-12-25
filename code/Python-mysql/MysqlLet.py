# -*- coding: utf-8 -*-
import pymysql

class MySQLet:
    '''类例化，处理一些连接操作'''
    def __init__(self,**kwargs):
        try:
            self._db = pymysql.connect(kwargs["host"],kwargs["user"],kwargs["password"],kwargs["database"] )
            self.__cursor = self._db.cursor()
            print("success")
        except Exception as e:
            print("数据库链接失败: %s" % e)
    def close(self):
        '''结束查询和关闭链接'''
        self._db.close()
    def create_table(self,sql_str):
        '''创建数据库'''
        try:
            self.__cursor.execute(sql_str)
            self._db.commit()
        except Exception as e:
            print(e)
            self._db.rollback()

    def query_formatrs(self,sql_str):
        '''查询数据，返回一个列表，里面的每一行是一个字典，带字段名
             cursor 为连接光标
             sql_str为查询语句'''
        try:
            self.__cursor.execute(sql_str)
            rows = self.__cursor.fetchall()
            r = []
            for row in rows:
                r.append(dict(zip(self.column_names(),row)))
            return r
        except Exception as e:
            print(e)
            # return False  
    def query(self,sql_str):
        '''查询数据并返回
             cursor 为连接光标
             sql_str为查询语句
        '''
        try:
            self.__cursor.execute(sql_str)
            rows = self.__cursor.fetchall()
            return rows       
        except Exception as e:
            print(e)

    def execute_update_insert(self,sql):
        '''
        插入或更新记录 成功返回最后的id
        '''
        self.__cursor.execute(sql)
        self._db.commit()
        return self.__cursor.lastrowid
    def column_names(self):
        '''查询字段'''
        columns = []
        for field in self.__cursor.description:
             columns.append(field[0])
        return columns