# -*- coding: UTF-8 -*-
from naoqi import ALProxy
import motion

import qi

# 连接到 NAO 机器人
robotIP = "192.168.43.250"
port = 9559


session = qi.Session()
session.connect("tcp://" + robotIP + ":" + str(port))

# 初始化代理
led_proxy = ALProxy("ALLeds", robotIP, port)

led_proxy.fadeRGB("AllLeds", "red", 1.0)  # 设置所有LED为红色，亮度为1.0

led_proxy.fadeRGB("FaceLeds", "blue", 0.5)  # 设置脸部LED为蓝色，亮度为0.5


