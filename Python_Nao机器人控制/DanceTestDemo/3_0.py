# -*- coding: UTF-8 -*-
from naoqi import ALProxy
import motion
import almath
import qi

# 创建与NAO机器人的会话

# ip
robotIP = "192.168.8.207"
# 端口
port = 9559
session = qi.Session()
session.connect("tcp://" + robotIP + ":" + str(port))

tts = ALProxy("ALTextToSpeech", robotIP , port)
tts.say("Hello, world!")


# motion = ALProxy("ALMotion", robotIP , port)
# tts    = ALProxy("ALTextToSpeech", robotIP , port)
# motion.setStiffnesses("Body", 1.0)
# motion.moveInit()
# motion.post.moveTo(0.5, 0, 0)
# tts.say("I'm walking")

# # 初始化代理
motionProxy  = ALProxy("ALMotion", robotIP, port)
postureProxy = ALProxy("ALRobotPosture", robotIP, port)
ttsProxy     = ALProxy("ALTextToSpeech", robotIP, port)
audioProxy   = ALProxy("ALAudioPlayer", robotIP, port)
#isAbsolute variable is used wherever functions require a boolean argument
# isAbsolute变量用于函数需要布尔参数的任何位置
isAbsolute   = True

# 笛卡尔控制
space      = motion.FRAME_ROBOT
axisMask   = almath.AXIS_MASK_ALL
#isAbsolute variable is used wherever functions require a boolean argument
#isAbsolute变量用于函数需要布尔参数的任何位置
isAbsolute = False


# 主要用到的函数方法为ALMotion.angelInterpolation方法控制机器人运动：
# 舞蹈动作一
def move1():

    names      = ["RHipRoll","LHipRoll", "LKneePitch"
                  , "LAnklePitch", "LHipPitch"]
    angleLists = [[0.2] ,[0.2]  ,[1]   ,[-0.5],[-0.5]]
    times      = [[1.0] ,[ 1.0] ,[1.0] ,[1.0] , [1.0]]
    isAbsolute = True
    motionProxy.angleInterpolation(names, angleLists, times, isAbsolute)

    names      = ["RShoulderRoll" ,"RHand","HeadYaw","LWristYaw"]
    angleLists = [[-1.5],[1,0,1,0]        ,[1.5] ,[-1.0]]
    times      = [[2.0] ,[0.5,1.0,1.5,2.0],[2.0] ,[1.0] ]
    isAbsolute = True
    motionProxy.angleInterpolation(names, angleLists, times, isAbsolute)

# 舞蹈动作二
def move2():
    names      = ["RHipRoll","LHipRoll" ,"LKneePitch"
                  ,"LAnklePitch" ,"LHipPitch"]
    angleLists = [[0],[0],[0],[0],[0]]
    times      = [[1.0],[ 1.0],[1.0],[1.0],[1.0]]
    isAbsolute = True
    motionProxy.angleInterpolation(names, angleLists, times, isAbsolute)


    motors  = ["RElbowRoll" ,"LElbowRoll","LShoulderRoll" ,"RShoulderPitch"
               ,"RHand", "LHand", "HeadYaw" ]
    angles  = [[0.5],[-0.5] ,[0.8],[-1] ,[1.0]  ,[1.0] , [0.7,0.7] ]
    times   = [[0.5],[0.5]  ,[0.5],[0.5],[0.5]  ,[0.5] , [0.5,1.0] ]
    motionProxy.angleInterpolation(motors, angles, times,isAbsolute)


    motors  = ["RElbowRoll","LElbowRoll","RShoulderRoll" ,"LShoulderPitch"
               ,"RHand", "LHand", "HeadYaw"   ]
    angles  = [[-0.5],[0.5] ,[-0.8] ,[1]    ,[1.0]  ,[1.0] , [-0.7,-0.7] ]
    times   = [[0.5] ,[0.5] ,[0.5]  ,[0.5]  ,[0.5]  ,[0.5] , [0.5,1]     ]
    motionProxy.angleInterpolation(motors, angles, times,isAbsolute)


    motors  = ["RElbowRoll","LElbowRoll","RShoulderPitch","LShoulderPitch"
               ,"RHand" ,"LHand" , "HeadYaw" ]
    angles  = [[0]  ,[0]    ,[-1]   ,[-1]   ,[-1.0]  ,[-1.0]  , [0] ]
    times   = [[0.3],[0.3]  ,[0.3]  ,[0.3]  ,[0.3]   ,[0.3]   , [0.3]]
    motionProxy.angleInterpolation(motors, angles, times,isAbsolute)

# 舞蹈动作三
def move3():


    Head_motors       = ["HeadPitch","HeadYaw"    ]
    Head_angles       = [[0.5,-0.5,0.5,-0.5,0.5,-0.5,0.5,-0.5,0.5,-0.5]
                         ,[1.0, -1.0]  ]
    Head_times        = [[0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0 ]
                         ,[ 2.5, 5.0]  ]

    UpperBody_motors  = ["RElbowRoll" ,"LElbowRoll"
                         ,"LShoulderPitch"  ,"RShoulderPitch"   ]
    UpperBody_angles  = [[0.5],[-0.5],[0.8, -0.8, 0.0, -0.8, 0.8]
                         ,[-0.8, 0.8, 0.0, 0.8, -0.8] ]
    UpperBody_times   = [[1.0],[1.0] ,[1.0,  2.0, 3.0,  4.0, 5.0]
                         ,[ 1.0, 2.0, 3.0, 4.0,  5.0] ]


    LowerBody_motors  = ["LKneePitch","RKneePitch","RAnklePitch","LAnklePitch"
                         ,"RHipPitch","LHipPitch"]
    LowerBody_angles  = [[1,0]  ,[1,0]  ,[-0.5,0] ,[-0.5,0]
                         ,[-0.5,0]   ,[-0.5,0]]
    LowerBody_times   = [[3,5]  ,[3,5]  ,[3,5]    ,[3,5]
                         ,[3,5]      ,[3,5]  ]

    #The motornames_names list has the various MOTOR_NAMES which are used
    #The angles list has the respective MOTOR_ANGLES which are used
    #The times list has the recpejtwctive TIMEs at which
    #the motor holds a particular angle value
    #motornames_names列表中有各种使用的MOTOR_NAME
    #角度列表中有各自使用的MOTOR_angles
    #时间列表具有可记录的活动时间
    #电机保持特定的角度值

    motor_names       = Head_motors + UpperBody_motors + LowerBody_motors
    times             = Head_times  + UpperBody_times  + LowerBody_times
    angles            = Head_angles + UpperBody_angles + LowerBody_angles
    isAbsolute = True


    motionProxy.angleInterpolation(motor_names, angles, times, isAbsolute)

    names =      ["RHand","RShoulderPitch"]
    angleLists = [[1.0],[-1.0]]
    times      = [[0.5],[0.5]] 
    motionProxy.angleInterpolation(names, angleLists, times, isAbsolute)

    #将NAO设置为初始姿势
    postureProxy.goToPosture("StandInit", 0.5)

# 舞蹈动作四
def move4():    

    #LOWER THE TORSO AND MOVE FROM SIDE TO SIDE
    #降低躯干，左右移动
    effector   = "Torso"
    path       = [0.0, -0.07, -0.03, 0.0, 0.0, 0.0]
    time       = 1.5                
    motionProxy.positionInterpolation(effector, space, path,axisMask
                                      , time, isAbsolute)

    effector   = "Torso"
    path       = [0.0, 0.07, 0.03, 0.0, 0.0, 0.0]
    time       = 1.5                
    motionProxy.positionInterpolation(effector, space, path,axisMask
                                      , time, isAbsolute)

    effector   = "Torso"
    path       = [0.0, 0.07, -0.03, 0.0, 0.0, 0.0]
    time       = 1.5                
    motionProxy.positionInterpolation(effector, space, path,axisMask
                                      , time, isAbsolute)

# 舞蹈动作五
def move5():

    Head_motors       = ["HeadPitch" ,"HeadYaw"    ]
    Head_angles       = [[0.5 ]      ,[1.0, -1.0]  ]
    Head_times        = [[0.5 ]      ,[ 2.5, 5.0]  ]

    UpperBody_motors  = ["RElbowRoll"   ,"LElbowRoll"
                         ,"LShoulderPitch"  ,"RShoulderPitch"]
    UpperBody_angles  = [[0.5]  ,[-0.5] ,[0.8,  0.8, 0.8,  0.8, 0]
                         ,[-0.8, -0.8, -0.8, -0.8,  0 ] ]
    UpperBody_times   = [[1.0]  ,[1.0]  ,[1.0,  2.0, 3.0,  4.0, 5.0]
                         ,[ 1.0, 2.0, 3.0, 4.0,  5.0] ]

    #The motornames_names list has the various MOTOR_NAMES which are used
    #The angles list has the respective MOTOR_ANGLES which are used
    #The times list has the recpective TIMEs at which
    #the motor holds a particular angle value

    #motornames_names列表中有各种使用的MOTOR_NAME
    #角度列表中有各自使用的MOTOR_angles
    #时间列表具有前瞻性TIME
    #电机保持特定的角度值

    motor_names       = UpperBody_motors + Head_motors
    times             = UpperBody_times  + Head_times
    angles            = UpperBody_angles + Head_angles

    isAbsolute = True
    motionProxy.angleInterpolation(motor_names, angles, times, isAbsolute)


def main(robotIP):    
    #机器人说出信息
    ttsProxy.say("I LIKE TO DANCE!")
    #我们将电机刚度设置为1，并引入NAO
    #舞蹈开始前的初始姿势
    #播放音乐
    motionProxy.setStiffnesses("Body", 1.0)
    postureProxy.goToPosture("StandZero", 0.5)
    audioProxy.post.playFile("C:\Users\coc\Desktop\music1\Paper Plane.mp3")
    #所有的舞步功能都是逐一调用的
    move1()
    move2()
    # move3()    
    # move4()
    # move5()
    #停止这首歌
    # audioProxy.stopAll()
    #设置NAO的初始姿势
    postureProxy.goToPosture("StandInit", 0.5)
    #机器人说出信息
    ttsProxy.say("THANK YOU!")
    #我们在舞蹈结束时将运动刚度设置为0
    motionProxy.setStiffnesses("Body", 0.0)


main(robotIP)

