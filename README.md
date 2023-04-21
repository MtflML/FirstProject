# Readme
## 准备
需要Python环境，设为私人项目
安装指定版本的Selenium和PhantomJS
```
pip install selenium==3.8.0
wget https://github.com/MtflML/PhantomJS/raw/main/phantomjs-2.1.1-linux-x86_64.tar.bz
tar -xjf phantomjs-2.1.1-linux-x86_64.tar.bz
rm -rf phantomjs-2.1.1-linux-x86_64.tar.bz
mv phantomjs-2.1.1-linux-x86_64 phantomjs
```
新建guaji.py，复制以下代码入内
```
# GoormIDE挂机脚本
# 假装在IDE，容器Always online
# -----------
# Ver0.1 by MtflML
# 请自行斟酌，当心号没
from selenium import webdriver
import time
import random
import os
browser=webdriver.PhantomJS(executable_path="./phantomjs/bin/phantomjs")
browser.implicitly_wait(30)
browser.get("https://accounts.goorm.io/login?return_url=aHR0cHM6Ly9pZGUuZ29vcm0uaW8vbXkvZGFzaGJvYXJkP3JlZGlyZWN0PTE=") 
browser.set_window_size(1920,1080)                                        
browser.find_element_by_name("email").send_keys(os.environ["DASHBOARD_USERNAME"])
browser.find_element_by_name("password").send_keys(os.environ["DASHBOARD_PASSWORD"])
browser.find_element_by_class("btn-primary").click()                               
browser.find_element_by_class("btn-outline-primary").click()              
while True:
    browser.execute(webdriver.remote.command.Command.MOVE_TO,{
        "xoffset":random.randint(0,1920),
        "yoffset":random.randint(0,1080)
    })                                                                    
    time.sleep(random.randint(0,10))
```
然后在主程序入口（默认为index.py）改为以下内容：
```
# GoormIDE 挂机脚本主程序
# 主进程启动主程序，子进程启动挂机
from multiprocessing import Process
def launch_guaji():
    import guaji
pr_guaji=Process(target=launch_guaji,args=())
# 用import方式启动真正的主程序，请按照自己项目要求自行添加
```
运行前请设定环境变量DASHBOARD_USERNAME登录邮箱DASHBOARD_PASSWORD登陆密码，然后在IDE界面内只需要启动修改过的主程序即可。

参考鸣谢：
=XHG78999= https://blog.csdn.net/weixin_43596804/article/details/121369601
ShadowObj https://github.com/ShadowObj/GoormKeepAlive
Chatgpt3.5
Claude
