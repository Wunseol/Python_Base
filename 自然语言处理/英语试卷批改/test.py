import SparkApi
#以下密钥信息从控制台获取
appid = "1a22b560"     #填写控制台中获取的 APPID 信息
api_secret = "NjRhMmMyYmYwM2RiNWUyMDExYmViOWZj"   #填写控制台中获取的 APISecret 信息
api_key ="b8a3a9ea2a7c0826bbd4c7c84d4d547c"    #填写控制台中获取的 APIKey 信息

#用于配置大模型版本，默认“general/generalv2”
domain = "generalv3"   # v3.0版本
# domain = "generalv2"    # v2.0版本
#云端环境的服务地址
# Spark_url = "ws://spark-api.xf-yun.com/v1.1/chat"  # v1.5环境的地址
# Spark_url = "ws://spark-api.xf-yun.com/v2.1/chat"  # v2.0环境的地址
Spark_url = "ws://spark-api.xf-yun.com/v3.1/chat"  # v3.0环境的地址

text =[]

# length = 0

def getText(role,content):
    jsoncon = {}
    jsoncon["role"] = role
    jsoncon["content"] = content
    text.append(jsoncon)
    return text

def getlength(text):
    length = 0
    for content in text:
        temp = content["content"]
        leng = len(temp)
        length += leng
    return length

def checklen(text):
    while (getlength(text) > 8000):
        del text[0]
    return text
    


if __name__ == '__main__':
    text.clear
    #       完成一个应用系统：功能批改英语课的试卷。试卷的题型分为两种：选择题和完型填空。
    #       考察的知识点为英语的语法。设计并实现一个应用程序，读入一份试卷，按照试卷的题目，自动产生正确答案。
    #       学生做题后，按照正确答案进行批改，算出分数。错误的题目给出参考答案。实现的平台语言以及数据库不限。
    #       上传整个项目以及相应的数据库表。
    #       注意：本题目中，题目和答案均为英文，不考虑特殊符号。
   
    Input = "你来批改英语课的试卷，题型分为两种：选择题和完型填空，我给出一份试卷的题目，你自动产生正确答案。我会在题目后面给出我的答案，你按照正确答案对我的答案进行批改，批改完后给出参考答案和分数（一题2分）。用中文回答"
    question = checklen(getText("user",Input))
    SparkApi.answer =""
    print("智能英语试卷批改:",end = "")
    SparkApi.main(appid,api_key,api_secret,Spark_url,domain,question)
    getText("assistant",SparkApi.answer)

    while(1):
        Input = input("\n" +"请输入题目和答案，不要有回车:")
        question = checklen(getText("user",Input))
        SparkApi.answer =""
        print("\n")
        print("智能英语试卷批改:",end = "")
        SparkApi.main(appid,api_key,api_secret,Spark_url,domain,question)
        getText("assistant",SparkApi.answer)
        # print(str(text))

