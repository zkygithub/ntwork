# -*- coding: utf-8 -*-
import sys
import time
import ntwork
from datetime import datetime
try:
    import schedule
except ImportError:
    print("Error: this example require schedule module, use `pip install schedule` install")
    sys.exit()

# 创建微信实例
wework = ntwork.WeWork()

# 打开pc企业微信, smart: 是否管理已经登录的微信
wework.open(smart=True)


# 发送文本消息任务
def send_text_job():
    if not wework.login_status:
        return
    human_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    wework.send_text(conversation_id="FILEASSIST", content=f"[ntwork] {human_time}")


# 设置调度的参数，这里是每5秒执行一次
schedule.every(5).seconds.do(send_text_job)


'''
# 每小时执行 
schedule.every().hour.do(job) 

# 每天12:25执行 
schedule.every().day.at("12:25").do(job) 

# 每2到5分钟时执行 
schedule.every(5).to(10).minutes.do(job) 

# 每星期4的19:15执行 
schedule.every().thursday.at("19:15").do(job) 

# 每第17分钟时就执行 
schedule.every().minute.at(":17").do(job)
'''

try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    ntwork.exit_()
    sys.exit()




