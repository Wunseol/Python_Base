# coding=utf-8

from naoqi import ALProxy
import math



robotIP = "169.254.114.88"
port = 9559

motionProxy = ALProxy("ALMotion", robotIP , port)

gyro_data = motionProxy.getRobotPosition(False)

print("Gyro Data: ", gyro_data)






