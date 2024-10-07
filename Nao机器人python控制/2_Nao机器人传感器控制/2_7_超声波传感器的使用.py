
# -*- encoding: UTF-8 -*-

"""Example: Use getData Method to Use Sonars Sensors"""

import qi
import argparse
import sys
import time

def main(session):
    """
    This example uses the getData method to use sonars sensors.
    """
    # 获取服务 ALMemory 和 ALSonar。

    memory_service = session.service("ALMemory")
    sonar_service = session.service("ALSonar")

    # 订阅声纳，启动声纳（硬件级）
    # 开始数据采集。
    sonar_service.subscribe("myApplication")

    # 从 ALMemory 检索声纳数据。

    print("Left Sonar Value:", memory_service.getData("Device/SubDeviceList/US/Left/Sensor/Value"))
    print("Right Sonar Value:", memory_service.getData("Device/SubDeviceList/US/Right/Sensor/Value"))
    # 取消订阅声纳，停止声纳（在硬件级别）
    sonar_service.unsubscribe("myApplication")



# robotIP = "169.254.114.88"
# port = 9559

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="169.254.114.88",
                        help="Robot IP address. On robot or Local Naoqi: use '169.254.114.88'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    while True:
     main(session)
     time.sleep(1)  # 设置适当的循环间隔时间


