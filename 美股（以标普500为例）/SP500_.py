#! -*- coding:utf-8 -*-


import datetime
import re
import time

import pymysql
import requests
from lxml import etree
from requests.exceptions import RequestException

def call_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None
def re_func(item_l):
    f_l =[]
    for item in item_l:

        patt =re.compile("\(.*?\)",re.S)
        ts = re.findall(patt,item)
        f_l.append(ts[0][1:-2])
    return f_l
# 正则和lxml混用
def parse_index(html):  # 正则专门有反爬虫的布局设置，不适合爬取表格化数据！

    selector = etree.HTML(html)
    Price = selector.xpath('//*[@id="spFP"]/div[1]/span[1]/text()')
    for item in Price:
        gi.append(item)

# 正则和lxml混用
def parse_detail(html):  # 正则专门有反爬虫的布局设置，不适合爬取表格化数据！
    selector = etree.HTML(html)
    re_item = selector.xpath('/html/body/div[1]/div[2]/div[1]/div/div/table/tbody/tr/td[7]/text()')
    vf = re_func(re_item)
    return vf

















def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='AT_Model',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:


        cursor.executemany('insert into sp500_AT (index_v,up_num,down_num,max_up,min_up,min_down,max_down) values (%s,%s,%s,%s,%s,%s,%s)', content)
        connection.commit()
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass



if __name__ == '__main__':
    gi = []
    positive_list = []
    negative_list =[]

    sp500_url = 'http://gu.qq.com/usINX/zs'
    sp500_detail = 'https://www.slickcharts.com/sp500'
    html_index = call_page(sp500_url)
    parse_index(html_index)


    html_detail = call_page(sp500_detail)

    re_item =parse_detail(html_detail)
    for item in re_item:
        if float(item) > 0:
            positive_list.append(item)
        elif float(item) < 0:
            negative_list.append(item)
    pos_len = len(positive_list)
    neg_len = len(negative_list)
    max_pos  = max(positive_list)
    min_pos  = min(positive_list)
    max_neg = min(negative_list)
    min_neg = max(negative_list)
    v_f = [pos_len,neg_len,max_pos,min_pos,max_neg,min_neg]
    ff_l = []
    f_tup = tuple(gi+v_f)
    ff_l.append((f_tup))
    insertDB(ff_l)











# index_v,up_num,down_num,max_up,min_up,min_down,max_down
# create table sp500_AT
# (id int not null primary key auto_increment,
# index_v  float,
#  up_num int,
#  down_num int,
#  max_up float,
#  min_up float,
#  min_down float,
#  max_down float,
# LastTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP) engine=InnoDB  charset=utf8;


# drop table nasdap100_s;


#  自动化模型跟踪
# * *  14-21 * * 1-5  sh /root/AT_sp500.sh
#
# 0 19 1,15 * *  /usr/local/bin/python3.6 /root/cron_SP500_.py
