# -*- coding: UTF-8 -*-
import time
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
# 连接到 NAO 机器人
# nao_ip = "127.0.0.1"  # 替换为你的 NAO 机器人的 IP 地址
# nao_port = 49917
session = qi.Session()
session.connect("tcp://" + robotIP + ":" + str(port))

# 初始化代理
motionProxy  = ALProxy("ALMotion", robotIP, port)
postureProxy = ALProxy("ALRobotPosture", robotIP, port)
ttsProxy     = ALProxy("ALTextToSpeech", robotIP, port)
audioProxy   = ALProxy("ALAudioPlayer", robotIP, port)
isAbsolute   = True # isAbsolute变量用于函数需要布尔参数的任何位置

# 设置手部关节的刚度
jointNames = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw",
              "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw"]
stiffnessList = 1.0  # 设置为1.0以保持固定姿势
motionProxy.setStiffnesses(jointNames, stiffnessList)

# 设置行走参数
X = 0.5  # 前进的距离（以米为单位）
Y = 0.0  # 左右移动的距离（以米为单位）
Theta = 0.0  # 转向角度（以弧度为单位）
Frequency = 0.3  # 步频
motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)

# 等待一段时间，使机器人行走
time.sleep(8.0)

# 停止行走
motionProxy.stopMove()

# 最后要释放手部关节的僵硬度
stiffnessList = 0.0  # 设置为0.0以释放关节
motionProxy.setStiffnesses(jointNames, stiffnessList)


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




