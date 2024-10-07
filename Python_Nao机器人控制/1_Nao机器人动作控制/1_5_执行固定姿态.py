# -*- coding: UTF-8 -*-
import time
from naoqi import ALProxy
import motion
import qi

# 创建与NAO机器人的会话

# # IP
# robotIP = "192.168.8.207"
# # 端口
# port = 9559

robotIP = "127.0.0.1"
port = 61237

session = qi.Session()
session.connect("tcp://" + robotIP + ":" + str(port))

# 初始化代理
motionProxy  = ALProxy("ALMotion", robotIP, port)
postureProxy = ALProxy("ALRobotPosture", robotIP, port)
ttsProxy     = ALProxy("ALTextToSpeech", robotIP, port)

ttsProxy.say("1_5_执行固定姿态")

# 初始化代理
motionProxy = ALProxy("ALMotion", robotIP , port)

#将运动刚度设置为1.0
# motionProxy.setStiffnesses("Body", 1.0)
# 执行moveInit()函数可以确保所有关节和传感器处于适当的状态，以便进行后续的动作控制和执行。
motionProxy.moveInit()

#将运动刚度设置为0.5---stiffness - 在0和1之间的一个或多个刚度参数。
motionProxy.setStiffnesses("Body", 0.5)

#设置NAO的初始姿势
postureProxy.goToPosture("StandInit", 0.5)
# postureProxy.goToPosture("StandInit", 1.0)指示机器人采取"StandInit"姿势，并在相对速度，大小为0.0-1.0

# 等待一段时间
# 使用time模块可以让程序休眠,具体方法是time.sleep(秒数),其中"秒数以秒为单位,
time.sleep(2.0)
postureProxy.goToPosture("Stand", 0.5)
time.sleep(2.0)
postureProxy.goToPosture("Sit", 0.5)


# 头部关节：

# HeadYaw（头部水平转动）
# HeadPitch（头部俯仰转动）
# 左臂关节：

# LShoulderPitch（左肩俯仰转动）
# LShoulderRoll（左肩水平转动）
# LElbowYaw（左肘关节水平转动）
# LElbowRoll（左肘关节俯仰转动）
# LWristYaw（左手腕水平转动）
# LHand（左手掌）
# LFinger（左手指）
# 右臂关节：

# RShoulderPitch（右肩俯仰转动）
# RShoulderRoll（右肩水平转动）
# RElbowYaw（右肘关节水平转动）
# RElbowRoll（右肘关节俯仰转动）
# RWristYaw（右手腕水平转动）
# RHand（右手掌）
# RFinger（右手指）
# 腿部关节：

# LHipYawPitch（左髋部水平俯仰转动）
# LHipRoll（左髋部水平转动）
# LHipPitch（左髋部俯仰转动）
# LKneePitch（左膝关节俯仰转动）
# LAnklePitch（左踝关节俯仰转动）
# LAnkleRoll（左踝关节摆动）
# RHipYawPitch（右髋部水平俯仰转动）
# RHipRoll（右髋部水平转动）
# RHipPitch（右髋部俯仰转动）
# RKneePitch（右膝关节俯仰转动）
# RAnklePitch（右踝关节俯仰转动）
# RAnkleRoll（右踝关节摆动）



