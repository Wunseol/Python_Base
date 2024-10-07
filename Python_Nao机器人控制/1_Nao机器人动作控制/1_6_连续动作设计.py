
# -*- coding: UTF-8 -*-
import time
from naoqi import ALProxy
import motion
import qi

# 创建与NAO机器人的会话
robotIP = "192.168.66.7"
port = 9559

# 初始化代理
motionProxy  = ALProxy("ALMotion", robotIP, port)
postureProxy = ALProxy("ALRobotPosture", robotIP, port)
ttsProxy     = ALProxy("ALTextToSpeech", robotIP, port)
# audioProxy   = ALProxy("ALAudioPlayer", robotIP, port)
isAbsolute   = True # isAbsolute变量用于函数需要布尔参数的任何位置

ttsProxy.say("1_6_连续动作设计")

# 主要用到的函数方法为ALMotion.angelInterpolation方法控制机器人运动：
# 舞蹈动作一
def move1():
   
    # 设置舞蹈动作
    names = ["LShoulderPitch", "RShoulderPitch"]
    angle_lists = [[1.0, 0.5, 1.0, 0.5], [0.5, 1.0, 0.5, 1.0]]  # 用于摆动的角度列表
    times = [[1.0, 2.0, 3.0, 4.0], [2.0, 3.0, 4.0, 5.0]]  # 对应每个角度的时间
    # 使用angleInterpolation设置舞蹈动作
    motionProxy.angleInterpolation(names, angle_lists, times, True)

def move1_1():

    # 设置舞蹈动作
    names = ["LShoulderPitch", "RShoulderPitch", "LShoulderRoll", "RShoulderRoll"]
    angle_lists = [
        [1.0, 0.5, 1.0, 0.5, 1.0, 0.5],
        [0.5, 1.0, 0.5, 1.0, 0.5, 1.0],
        [0.5, 0.8, 0.5, 0.8, 0.5, 0.8],
        [0.8, 0.5, 0.8, 0.5, 0.8, 0.5]
    ]  # 用于摆动的角度列表
    times = [
        [1.0, 2.0, 3.0, 4.0, 5.0, 6.0],
        [2.0, 3.0, 4.0, 5.0, 6.0, 7.0],
        [1.0, 2.0, 3.0, 4.0, 5.0, 6.0],
        [2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
    ]  # 对应每个角度的时间
    # 使用angleInterpolation设置舞蹈动作
    motionProxy.angleInterpolation(names, angle_lists, times, True)

def move1_1_1():

    # 设置更多的舞蹈动作
    names = ["LShoulderPitch", "RShoulderPitch", "LElbowYaw", "RElbowYaw", "LHipYawPitch", "RHipYawPitch"]
    angle_lists = [
        [1.0, 0.5, 1.0, 0.5, 1.0, 0.5],
        [0.5, 1.0, 0.5, 1.0, 0.5, 1.0],
        [0.3, 0.5, 0.3, 0.5, 0.3, 0.5],
        [0.5, 0.3, 0.5, 0.3, 0.5, 0.3],
        [0.2, -0.2, 0.2, -0.2, 0.2, -0.2],
        [-0.2, 0.2, -0.2, 0.2, -0.2, 0.2]
    ]  # 用于摆动的角度列表
    times = [
        [1.0, 2.0, 3.0, 4.0, 5.0, 6.0],
        [2.0, 3.0, 4.0, 5.0, 6.0, 7.0],
        [1.0, 2.0, 3.0, 4.0, 5.0, 6.0],
        [2.0, 3.0, 4.0, 5.0, 6.0, 7.0],
        [1.0, 2.0, 3.0, 4.0, 5.0, 6.0],
        [2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
    ]  # 对应每个角度的时间
    # 使用angleInterpolation设置舞蹈动作
    motionProxy.angleInterpolation(names, angle_lists, times, True)

def move1_1_1_1():

    # 执行招手动作
    names = ["RShoulderRoll", "RElbowRoll", "RHand", "LShoulderRoll", "LElbowRoll", "LHand"]
    angles = [0.5, 0.5, 1.0, -0.5, -0.5, 1.0]
    times = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

    motionProxy.angleInterpolation(names, angles, times, True)



# 舞蹈动作二
def move2():

    motors  = ["LShoulderRoll" ,"RShoulderPitch"]
    angles  = [[-0.3,0.3],[-0.3,0.3] ]
    times   = [[1.0,3.0],[2.0,3.0] ]
    motionProxy.angleInterpolation(motors, angles, times,isAbsolute)


# 舞蹈动作三
def move3():

    Head_motors       = ["HeadPitch","HeadYaw"    ]
    Head_angles       = [[0.2,-0.2,0.2,-0.2,0.2,-0.2,0.2,-0.2,0.2,-0.2],[0.3, -0.3]  ]
    Head_times        = [[0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0 ],[ 2.5, 5.0]  ]

    UpperBody_motors  = ["LShoulderPitch"  ,"RShoulderPitch"  ]
    UpperBody_angles  = [[0.3, -0.3, 0.0, -0.3, 0.3],[-0.3, 0.3, 0.0, 0.3, -0.3] ]
    UpperBody_times   = [[1.0,  2.0, 3.0,  4.0, 5.0],[ 1.0, 2.0, 3.0, 4.0,  5.0] ]
    
    #motornames_names列表中有各种使用的MOTOR_NAME
    motor_names = Head_motors + UpperBody_motors#角度列表中有各自使用的MOTOR_angles
    angles = Head_angles + UpperBody_angles#电机保持特定的角度值
    times = Head_times  + UpperBody_times #时间列表具有可记录的活动时间
    
    motionProxy.angleInterpolation(motor_names, angles, times, True)



def main(robotIP):   
    # 等待一段时间
    time.sleep(1.0)
    ttsProxy.say("I LIKE TO DANCE!") #机器人说出信息
    motionProxy.setStiffnesses("Body", 1.0)#将电机刚度设置为1，并引入NAO
    postureProxy.goToPosture("StandZero", 0.5)#舞蹈开始前的初始姿势
    # audioProxy.post.playFile("C:\Users\coc\Desktop\music1\PaperPlane.mp3")#播放音乐
    
    #舞步逐一调用
# ==============================================================
    # ttsProxy.say("111111111") #机器人说出信息
    move1() # 动动手 ok
    postureProxy.goToPosture("StandInit", 0.5)#设置NAO的初始姿势
    # time.sleep(1.0)
# ==============================================================
    # ttsProxy.say("222222222") #机器人说出信息
    move1_1() # 动动手 ok
    postureProxy.goToPosture("StandInit", 0.5)#设置NAO的初始姿势
    # time.sleep(1.0)
# ==============================================================
    # ttsProxy.say("333333333") #机器人说出信息
    move1_1_1() # 动动腿 ok
    postureProxy.goToPosture("StandInit", 0.5)#设置NAO的初始姿势
    # time.sleep(1.0)
# ==============================================================
    # ttsProxy.say("444444444") #机器人说出信息
    move1_1_1_1() # 伸伸手 ok
    postureProxy.goToPosture("StandInit", 0.5)#设置NAO的初始姿势
    # time.sleep(1.0)
# ==============================================================
    # ttsProxy.say("555555555") #机器人说出信息
    move2() # 动动手 ok
    postureProxy.goToPosture("StandInit", 0.5)#设置NAO的初始姿势
    # time.sleep(1.0)
# ==============================================================
    # ttsProxy.say("666666666") #机器人说出信息
    move3()   # 摆摆手 ok 
    move3()   # 摆摆手 ok 
    move3()   # 摆摆手 ok 
    move3()   # 摆摆手 ok 
    postureProxy.goToPosture("StandInit", 0.5)#设置NAO的初始姿势
    # time.sleep(1.0)
# ==============================================================
    # audioProxy.stopAll()#停止这首歌
    ttsProxy.say("THANK YOU!") #机器人说出信息
    motionProxy.setStiffnesses("Body", 0.8)#我们在舞蹈结束时将运动刚度设置为0.8


main(robotIP)


