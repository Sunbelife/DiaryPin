#encoding = utf-8
# 2018.4.24 Sunbelife
import time
from xpinyin import Pinyin
from urllib import request
from pyquery import PyQuery as pq
import json
import pyperclip

with request.urlopen('http://pv.sohu.com/cityjson') as f:
	city_info = f.read()
	data = json.loads(city_info.decode('gbk')[18:-1])
	curr_local = data['cname']
	curr_local = curr_local.split('省')[1].split('市')[0]
	
#curr_local = "深圳" # 也可以手动写地点
curr_py_local = Pinyin().get_pinyin(curr_local, '')
ch_week = ["一","二","三","四","五","六","日"]
localtime = time.localtime(time.time())
localtime = ("{} 年 {} 月 {} 日 | 周 {}".format(localtime[0], localtime[1], localtime[2], ch_week[localtime[6]]))

url = "http://i.tianqi.com/index.php?c=code&id=8&icon=1&py=" + curr_py_local + "&num=1"

with request.urlopen(url) as f:
	data = f.read()
	d = pq(data.decode('utf-8'))
	today_weather = d('div').filter('#day_1').text()[3:]
	
pin = "气温：" + today_weather + " | 地点：" + curr_local

print(localtime + "\n" + pin)
pyperclip.copy(localtime + "\n" + pin)