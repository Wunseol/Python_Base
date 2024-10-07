# -*- coding: UTF-8 -*-


#未成功，如果你实现了可以提交一份


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
# robotIP = "127.0.0.1"
# port = 49917
robotIP = "192.168.22.7"
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
# 连接到机器人的代理

tts = ALProxy("ALTextToSpeech", robotIP , port)

tts.say("1")

# 播放本地音乐文件
# file_path = "PaperPlane.mp3"  # 请将其替换为实际的音乐文件路径
# audioProxy.playFile(file_path)
# audioProxy.post.playFile(r"C:\Users\coc\Desktop\music1\PaperPlane.mp3")#播放音乐

# # 播放本地音频文件
# fileId = audioProxy.loadFile("C:\Users\coc\Desktop\music1\PaperPlane.mp3")
# audioProxy.play(fileId)
# time.sleep(2)
# audioProxy.stopAll()#停止这首歌



# # 加载音乐文件
# audioProxy.loadFile(r"C:\Users\coc\Desktop\music1\PaperPlane.mp3")
# # 播放音乐
# audioProxy.play()


# audio_proxy = ALProxy("ALAudioPlayer", robotIP, port)

# music_file = "C:/Users/coc/Desktop/music1/PaperPlane.mp3"  # 请替换为你的音乐文件路径
# audio_proxy.playFile(music_file)
audio_player = ALProxy("ALAudioPlayer", robotIP, port)

# 设置音乐文件的路径
music_file = "C:/Users/coc/Desktop/music1/PaperPlane.mp3"
# 播放音乐
audio_player.playFile(music_file)

# 等待音乐播放完成
while audio_player.isPlaying():
    time.sleep(0.1)

