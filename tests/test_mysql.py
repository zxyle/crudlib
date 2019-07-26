#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@zxyle.cn>
# Date: 2019/7/26
# Desc: 


from tinycrud.mysql import MySQL

my = MySQL("mysql+pymysql://root:@localhost:3306/test?charset=utf8mb4")


def test_insert():
    table_name = "students"
    my.create_tb(table_name)
    my.insert(table_name, {"name": "zx", "age": 1, "address": "Hangzhou"})
    rows = my.query(table_name, {})
    assert type(rows) is dict