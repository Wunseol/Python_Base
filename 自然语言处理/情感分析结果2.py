from snownlp import SnowNLP

def analyze_sentiment_chinese(text):
    # 创建 SnowNLP 对象
    s = SnowNLP(text)
    
    # 获取情感分数（范围从0到1，其中0表示负面，1表示正面）
    sentiment_score = s.sentiments
    
    # 根据分数对情感进行分类
    sentiment = "正面" if sentiment_score > 0.5 else "负面"
    
    return sentiment, sentiment_score

# 提供一个示例句子
sample_sentence_chinese = "小明是一个很聪明的学生。"

# 使用 SnowNLP 进行情感分析
sentiment_result, sentiment_score = analyze_sentiment_chinese(sample_sentence_chinese)

# 打印情感分析结果和分数
print(f"情感: {sentiment_result}")
print(f"情感分数: {sentiment_score}")
