from stanfordcorenlp import StanfordCoreNLP
# 创建StanfordCoreNLP对象，指定Stanford CoreNLP工具包的路径和语言为中文
nlp = StanfordCoreNLP(r"C:\Users\coc\Desktop\stanford-corenlp-full-2018-10-05", lang="zh")
# 计算给定词条在文本中出现的频率

def count_word_frequency(text, word):
    words = text.split()
    count = 0
    for w in words:
        if w == word:
            count += 1
    return count

text = "这是一个示例文本，用于计算给定中文词条在中文文本中出现的频率。"
word = "示例"
frequency = count_word_frequency(text, word)
print(f"词条 '{word}' 在文本中出现了 {frequency} 次。")

