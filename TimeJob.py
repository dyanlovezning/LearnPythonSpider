# -*- coding:utf-8 -*-

import datetime
import schedule
import time
from CityCode import *
from SpiderWeath import *
from SendEmail import *


from wxpy import *
bot = Bot(cache_path = True)   #定义一个微信机器人

# 获取所有好友
friends = bot.friends()

# 遍历输出好友名称
#for friend in friends:
#    print(friend)
print(friends.count)

# 搜索名称包含 '游否' 的深圳男性好友
found = bot.friends().search('刘扬', sex=MALE)
print(found)
# [<Friend: 游否>]
# 确保搜索结果是唯一的，并取出唯一结果
youfou = ensure_one(found)
# <Friend: 游否>
    
    
def run():
    city_code = City()
    city_code.load('city_code.txt') 
    str = city_code.find_code("深圳")
    
    weath = getWeath(str)
    print(weath)
    print(type(weath))
    
    sendtext = "";
    for key, value in weath.items():
      sendtext += "%s:%s\n" % (key, value)
    #sendWeatherMsg(receivers, weath)
    ret = send_email("260680524@qq.com", sendtext)


#schedule.every(10).seconds.do(run)
#schedule.every(10).seconds.do(job2)


'''
while True:
    print("#")
    #run()

    bot = Bot()

    # 机器人账号自身
    myself = bot.self

    # 向文件传输助手发送消息
    bot.file_helper.send('Hello from wxpy!')
    #schedule.run_pending()
    time.sleep(100)
'''