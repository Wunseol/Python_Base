# coding=utf-8
from naoqi import ALProxy
import time


robotIP = "169.254.114.88"
port = 9559

memory = ALProxy("ALMemory", robotIP, port)

LFoot_Front = "Device/SubDeviceList/LFoot/FSR/FrontLeft/Sensor/Value"
LFoot_Rear = "Device/SubDeviceList/LFoot/FSR/RearLeft/Sensor/Value"
RFoot_Front = "Device/SubDeviceList/RFoot/FSR/FrontRight/Sensor/Value"
RFoot_Rear = "Device/SubDeviceList/RFoot/FSR/RearRight/Sensor/Value"

# 在循环中获取传感器数据
while True:
  LFoot_Front_value = memory.getData(LFoot_Front)
  LFoot_Rear_value = memory.getData(LFoot_Rear)
  RFoot_Front_value = memory.getData(RFoot_Front)
  RFoot_Rear_value = memory.getData(RFoot_Rear)
  print(LFoot_Front_value)
  print(LFoot_Rear_value)
  print(RFoot_Front_value)
  print(RFoot_Rear_value)
  print()

  # 对数据进行处理或判断

  time.sleep(4) # 设置适当的循环间隔时间


  