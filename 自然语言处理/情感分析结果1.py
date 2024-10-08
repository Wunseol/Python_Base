import json
from stanfordcorenlp import StanfordCoreNLP

# 创建 StanfordCoreNLP 对象，指定 Stanford CoreNLP 工具包的路径和语言为中文
nlp = StanfordCoreNLP(r"C:\Users\coc\Desktop\stanford-corenlp-full-2018-10-05", lang="zh")

# 进行情感分析的文本
text ="这是一部令人振奋的电影，充满了希望和正能量，演员们的表演非常出色，故事情节引人入胜，让人不禁为主人公的成功而欢欣鼓舞，这部作品让观众充满了愉悦和乐观的情绪，是一部不容错过的佳作，这是一部令人振奋的电影，充满了希望和正能量，演员们的表演非常出色，故事情节引人入胜，让人不禁为主人公的成功而欢欣鼓舞，这部作品让观众充满了愉悦和乐观的情绪，是一部不容错过的佳作"
# text ="这是一部电影"
# 使用 Stanford CoreNLP 对文本进行情感分析，返回 JSON 格式的结果
result = nlp.annotate(text, properties={
                       'annotators': 'sentiment',
                       'outputFormat': 'json',
                       'timeout': 10000,
                   })

print(result)

# 将 JSON 字符串解析为字典
result_dict = json.loads(result)
print(111111111111112222222222222222222222222222)
print(result_dict['sentences'])
print(1111111111111122222222222222222222221)
# 分析结果为一个字典，获取 'sentences' 键对应的值
sentiments = []
for sentence in result_dict['sentences']:
    sentiment_value = sentence['sentimentValue']
    
    print("11111111111111111111111")
    print(sentiment_value)
    print("11111111111111111111111")

    sentiment = 'Positive' if sentiment_value >= '3' else 'Negative' if sentiment_value == '0' else 'Neutral'
    sentiments.append(sentiment)

# 打印详细情感分析结果
print(result_dict)

# 打印情感分析结果
print(sentiments)

# 关闭 StanfordCoreNLP 对象
nlp.close()
