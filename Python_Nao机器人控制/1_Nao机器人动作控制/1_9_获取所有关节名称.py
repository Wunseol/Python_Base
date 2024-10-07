# -*- coding: UTF-8 -*-
from naoqi import ALProxy
import motion
import almath
import qi

# 创建与NAO机器人的会话

# # IP
# robotIP = "192.168.8.207"
# # 端口
# port = 9559

robotIP = "169.254.114.88"
port = 9559

session = qi.Session()
session.connect("tcp://" + robotIP + ":" + str(port))

# 初始化代理
motionProxy  = ALProxy("ALMotion", robotIP, port)


# 获取头部摄像头的当前位置
cameraAngle = motionProxy.getAngles("HeadPitch", True)  # True 表示使用弧度
# 打印摄像头角度
print("print:")
print("Camera Angle:", cameraAngle)

# 获取所有关节名称
jointNames = motionProxy.getJointNames("Body")
# 打印所有关节名称
print("print:")
print(jointNames)



