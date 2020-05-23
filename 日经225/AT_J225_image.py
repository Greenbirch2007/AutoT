import re
import time
import urllib.request

from retrying import retry
from urllib.error import URLError
import os

import time


def retry_if_io_error(exception):
    return isinstance(exception,URLError)

#  重复请求
@retry(retry_on_exception=retry_if_io_error)
def call_url():
    l_path = os.getcwd()
    image_Tname = time.strftime("%Y-%m-%d", time.localtime())
    url = 'https://chart.yahoo.co.jp/?code=998407.O&tm=1d&vip=off'
    urllib.request.urlretrieve(url, '{0}/{1}.jpg'.format(l_path,image_Tname))




if __name__=='__main__':
    call_url()
    print("图片下载完毕")

