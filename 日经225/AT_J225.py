#coding=utf-8

# 这里必须使用协程了！
import datetime
import re
import time

import pymysql
import requests
from lxml import etree
import json
from queue import Queue
import threading
from requests.exceptions import RequestException




from retrying import retry

def retry_if_io_error(exception):
    return isinstance(exception, ZeroDivisionError)




'''
1. 创建 URL队列, 响应队列, 数据队列 在init方法中
2. 在生成URL列表中方法中,把URL添加URL队列中
3. 在请求页面的方法中,从URL队列中取出URL执行,把获取到的响应数据添加响应队列中
4. 在处理数据的方法中,从响应队列中取出页面内容进行解析, 把解析结果存储数据队列中
5. 在保存数据的方法中, 从数据队列中取出数据,进行保存
6. 开启几个线程来执行上面的方法
'''

def run_forever(func):
    def wrapper(obj):
        while True:
            func(obj)
    return wrapper










def re_func(item_l):
    f_l =[]
    item_s = item_l[0]
    patt =re.compile("\（.*?\）",re.S)
    ts = re.findall(patt,item_s)
    f_l.append(ts[0][1:-2])
    return f_l






def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JS_Mons',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()

    try:
        # 用一个列表解析
        f_jsp = ["J" + str(cod) for cod in jl]
        sp_func = lambda x: ",".join(x)
        f_lcode = sp_func(f_jsp)

        f_ls = "%s," * len(jl)# 这里错了
        cursor.executemany('insert into sp_LJ ({0}) values ({1})'.format(f_lcode, f_ls[:-1]), content)
        connection.commit()
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError:
        pass



#










def run_forever(func):
    def wrapper(obj):
        while True:
            func(obj)
    return wrapper


def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JS225_JS400',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()

    try:
        js225 = 'J9984,J9983,J9766,J9735,J9613,J9602,J9532,J9531,J9503,J9502,J9501,J9437,J9433,J9432,J9412,J9301,J9202,J9107,J9104,J9101,J9064,J9062,J9022,J9021,J9020,J9009,J9008,J9007,J9005,J9001,J8830,J8804,J8802,J8801,J8795,J8766,J8750,J8729,J8725,J8630,J8628,J8604,J8601,J8411,J8355,J8354,J8331,J8316,J8309,J8308,J8306,J8304,J8303,J8267,J8253,J8252,J8233,J8058,J8053,J8035,J8031,J8028,J8015,J8002,J8001,J7951,J7912,J7911,J7832,J7762,J7752,J7751,J7735,J7733,J7731,J7272,J7270,J7269,J7267,J7261,J7211,J7205,J7203,J7202,J7201,J7186,J7013,J7012,J7011,J7004,J7003,J6988,J6976,J6971,J6954,J6952,J6902,J6857,J6841,J6770,J6762,J6758,J6752,J6724,J6703,J6702,J6701,J6674,J6645,J6506,J6504,J6503,J6501,J6479,J6473,J6472,J6471,J6367,J6361,J6326,J6305,J6302,J6301,J6178,J6113,J6103,J6098,J5901,J5803,J5802,J5801,J5714,J5713,J5711,J5707,J5706,J5703,J5631,J5541,J5411,J5406,J5401,J5333,J5332,J5301,J5233,J5232,J5214,J5202,J5201,J5108,J5101,J5020,J5019,J4911,J4902,J4901,J4755,J4751,J4704,J4689,J4631,J4578,J4568,J4543,J4523,J4519,J4507,J4506,J4503,J4502,J4452,J4324,J4272,J4208,J4188,J4183,J4151,J4063,J4061,J4043,J4042,J4021,J4005,J4004,J3863,J3861,J3436,J3407,J3405,J3402,J3401,J3382,J3289,J3105,J3103,J3101,J3099,J3086,J2914,J2871,J2802,J2801,J2768,J2531,J2503,J2502,J2501,J2432,J2413,J2282,J2269,J2002,J1963,J1928,J1925,J1812,J1808,J1803,J1802,J1801,J1721,J1605,J1333,J1332'

        f_225 = "%s," * 225
        cursor.executemany('insert into js225_s ({0}) values ({1})'.format(js225, f_225[:-1]), content)
        connection.commit()
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError:
        pass
def RemoveDot(item):
    f_l = []
    for it in item:

        f_str = "".join(it.split(","))
        ff_str = f_str +"00"
        f_l.append(ff_str)

    return f_l

def remove_douhao(num):
    num1 = "".join(num.split(","))
    f_num = str(num1)
    return f_num
def remove_block(items):
    new_items = []
    for it in items:
        f = "".join(it.split())
        new_items.append(f)
    return new_items
class QiubaiSpider(object):


    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
        }
        self.url_pattern = "https://stocks.finance.yahoo.co.jp/stocks/detail/?code={0}.T"
        # url 队列
        self.url_queue = Queue()
        # 响应队列
        self.page_queue = Queue()
        # 数据队列
        self.data_queue = Queue()


    def add_url_to_queue(self):
        # 把URL添加url队列中
        # js225_l =  [6857,9984,9983,6971,6954,6762,8035,7751,7267,4502,7203,4063,9433,9735,6758,8253,9737,4523,9613,3382,4503,6902,4324,4901,6367,4704,4543,7733,4452,9766,6366,8830,8267,8058,6752,8802,4568,1963,8801,7269,5108,8252,7752,6473,6841,8766,8604,8238,9064,4519,7912,6753,4911,6301,5901,7731,7951,6952,4021,6773,2914,1925,6976,6770,9301,1928,5802,8233,8306,8309,1721,5201,4507,1601,5333,8031,2502,8755,8053,5713,2503,6767,7911,6103,4902,8752,7201,8601,3405,6991,5002,5714,4506,8316,5803,2802,3105,2002,6326,8403,2801,2282,8355,8583,7762,6302,5707,4272,5332,8001,8331,3404,8411,6702,4183,8332,6503,2602,4151,3402,5801,5016,8603,5001,6471,4005,1802,6472,9104,8803,9020,6501,8795,3407,5706,3401,1803,7205,9101,9605,3861,9009,8303,9005,5631,6701,9107,9008,9007,2531,6479,3865,1812,2779,6502,6361,7261,5301,9681,7270,5101,4042,2261,5711,9062,2202,8606,9001,6504,8002,2501,1801,2001,7011,9531,2871,9432,4045,3893,5233,4061,5202,5405,4004,7231,9021,1861,1332,9202,6508,5401,9532,4041,5406,5411,7202,7012,8308,4188,3101,6703,7013,5232,4208,7003,8404,5701,9205,3110,6674,9501,9502,6764,5715,4689,9503,7211,3864,6796,3103,7004,8003,9437,4795,2768]
        js225_l =  [6857,9984,9983,6971]

        for i in js225_l:
            time.sleep(0.1)
            self.url_queue.put(self.url_pattern.format(i))

    @run_forever
    def add_page_to_queue(self):
        ''' 发送请求获取数据 '''
        url = self.url_queue.get()
        # print(url)
        response = requests.get(url, headers=self.headers)
        print(response.status_code)
        print(datetime.datetime.now())
        if response.status_code != 200:
            self.url_queue.put(url)
        else:
            self.page_queue.put(response.content)
        # 完成当前URL任务
        self.url_queue.task_done()

    @run_forever
    def add_dz_to_queue(self):
        '''根据页面内容使用lxml解析数据, 获取段子列表'''
        page = self.page_queue.get()
        try:

            patt = re.compile(
                '<td class="change"><span class="yjSt">前日比</span><span class="icoDownRed yjMSt">(.*?)</span></td>', re.S)
            # 避免报错TypeError: cannot use a string pattern on a bytes-like object
            item = re.findall(patt, page.decode("utf-8"))
            re_item = re_func(item)
            for item in re_item:
                if float(item) > 0:
                    positive_list.append(item)
                elif float(item) < 0:
                    negative_list.append(item)
                else:
                    pass


            self.page_queue.task_done()
        except:
            pass

    def get_first_element(self, list):
        '''获取列表中第一个元素,如果是空列表就返回None'''
        return list[0] if len(list) != 0 else None







    def run_use_more_task(self, func, count=1):
        '''把func放到线程中执行, count:开启多少线程执行'''
        for i in range(0, count):
            t = threading.Thread(target=func)
            t.setDaemon(True)
            t.start()

    def run(self):
        # 开启线程执行上面的几个方法
        url_t = threading.Thread(target=self.add_url_to_queue)
        # url_t.setDaemon(True)
        url_t.start()

        self.run_use_more_task(self.add_page_to_queue, 10)
        self.run_use_more_task(self.add_dz_to_queue, 9)


        # 使用队列join方法,等待队列任务都完成了才结束
        self.url_queue.join()
        self.page_queue.join()



def getIndex():
    url = 'https://stocks.finance.yahoo.co.jp/stocks/detail/?code=998407.O'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:

        page = response.text

        patt = re.compile(
            '<td class="change"><span class="yjSt">前日比</span><span class="icoDownRed yjMSt">(.*?)</span></td>', re.S)
        # 避免报错TypeError: cannot use a string pattern on a bytes-like object
        item = re.findall(patt, page.decode("utf-8"))
        re_item = re_func(item)
        return re_item
    else:
        pass





if __name__ == '__main__':
    gi = getIndex()
    print(gi)
    # qbs = QiubaiSpider()
    # qbs.run()
    positive_list =[]
    negative_list = []
    #





    # f_tup = tuple(big_list)
    # ff_l.append((f_tup))



    pos_len= len(positive_list)
    neg_len= len(negative_list)

    if pos_len != 0 and neg_len !=0:


        max_pos  = max(positive_list)
        min_pos  = min(positive_list)
        max_neg = min(negative_list)
        min_neg = max(negative_list)
        gi = getIndex()
        fl= pos_len+neg_len+max_pos+min_pos+max_neg+min_neg+gi
        print(fl)



