# coding=utf-8

from naoqi import ALProxy

robotIP = "169.254.114.88"
port = 9559


motionProxy = ALProxy("ALMotion", robotIP , 9559)

# 获取关节角度传感器数据
joint_names = ["HeadYaw", "HeadPitch", "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw",
             "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw"]  # 要获取数据的关节名称
use_sensors = True  # 是否使用传感器数据而非运动学数据
angles = motionProxy.getAngles(joint_names, use_sensors)  # 获取关节角度数据

# 打印关节角度数据
for i in range(len(joint_names)):
    print(joint_names[i] + ": " + str(angles[i]))


