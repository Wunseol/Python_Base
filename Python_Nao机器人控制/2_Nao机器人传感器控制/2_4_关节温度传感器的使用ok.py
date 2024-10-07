# -*- coding: UTF-8 -*-
from naoqi import ALProxy
import qi

# 连接到 NAO 机器人
robotIP = "169.254.114.88"
port = 9559

session = qi.Session()
session.connect("tcp://" + robotIP + ":" + str(port))

# 初始化代理
memory_service = ALProxy("ALMemory", robotIP , port)
motionProxy  = ALProxy("ALMotion", robotIP, port)
ttsProxy     = ALProxy("ALTextToSpeech", robotIP, port)

ttsProxy.say("2_4_关节温度传感器的使用")


joint_name1 = "RHand"
temperature = memory_service.getData("Device/SubDeviceList/{0}/Temperature/Sensor/Value".format(joint_name1))
print("关节RHand的温度：{1}".format(joint_name1, temperature))

joint_name2 = "LHand"
temperature = memory_service.getData("Device/SubDeviceList/{0}/Temperature/Sensor/Value".format(joint_name2))
print("关节LHand的温度：{1}".format(joint_name2, temperature))

joint_name3 = "Head"
temperature = memory_service.getData("Device/SubDeviceList/{0}/Temperature/Sensor/Value".format(joint_name3))
print("关节Head的温度：{1}".format(joint_name3, temperature))



