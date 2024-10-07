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
robotIP = "127.0.0.1"
# 端口
port = 49917

# 连接到 NAO 机器人
# nao_ip = "127.0.0.1"  # 替换为你的 NAO 机器人的 IP 地址
# nao_port = 49917


session = qi.Session()
session.connect("tcp://" + robotIP + ":" + str(port))



tts = ALProxy("ALTextToSpeech", robotIP , port)
tts.say("啊这11")


# motion = ALProxy("ALMotion", robotIP , port)
# tts    = ALProxy("ALTextToSpeech", robotIP , port)
# motion.setStiffnesses("Body", 1.0)
# motion.moveInit()
# motion.post.moveTo(0.5, 0, 0)
# tts.say("I'm walking")



