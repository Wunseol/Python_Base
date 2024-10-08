
from stanfordcorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP(r"C:\Users\coc\Desktop\stanford-corenlp-full-2018-10-05", lang = "zh")

# string = "小明硕士毕业于中国科学院计算所，后在日本京都大学深造。"
# print(string,type(string))

# # nlp下有很多可供使用的函数
# # 1.命名实体的识别
# string_ner = nlp.ner(string)
# print(type(string_ner))# list类型
# print(type(string_ner[0]))# list中每个元素是一个元组
# print(string_ner)
# print("*"*10)

# # 2.词性标注
# string_pos = nlp.pos_tag(string)
# print(type(string_pos))# list类型
# print(type(string_pos[0]))# list中每个元素是一个元组
# print(string_pos)


from stanfordcorenlp import StanfordCoreNLP
# 创建StanfordCoreNLP对象，指定Stanford CoreNLP工具包的路径和语言为中文
nlp = StanfordCoreNLP(r"C:\Users\coc\Desktop\stanford-corenlp-full-2018-10-05", lang="zh")
# 计算给定词条在文本中出现的频率
print("计算给定词条在文本中出现的频率：")
def calculate_word_frequency_chinese(text, target_word):
    # 使用Stanford CoreNLP的分词工具将中文文本切分成词语列表
    words = nlp.word_tokenize(text)
    print(words)
    # 计算目标词条在词语列表中的出现次数
    frequency = words.count(target_word)
    return frequency
# 示例中文文本
sample_text_chinese = "计算给定词条在文本中出现的频率，计算目标词条在词语列表中的出现次数，这是一个示例文本，示例文本包含了一些示例词语。"
# 要计算的目标词条
target_word_chinese = "示例"
# 计算目标词条在中文文本中的出现频率
word_frequency_chinese = calculate_word_frequency_chinese(sample_text_chinese, target_word_chinese)
# 打印结果
print(f"词语 '{target_word_chinese}' 在文本中出现了 {word_frequency_chinese} 次。")
print()


# from stanfordcorenlp import StanfordCoreNLP
# # 创建StanfordCoreNLP对象，指定Stanford CoreNLP工具包的路径和语言为中文
# nlp = StanfordCoreNLP(r"C:\Users\coc\Desktop\stanford-corenlp-full-2018-10-05", lang="zh")
print("对于一段你给出的文字，进行分词，用NLP的可以使用中文文本：")
# 示例中文文本
sample_text_chinese = "小明硕士毕业于中国科学院计算所，后在日本京都大学深造。小明是一个很聪明的学生。"
# 使用Stanford CoreNLP的分词工具将中文文本切分成词语列表
words = nlp.word_tokenize(sample_text_chinese)
# 打印分词结果
print(words)
print()
# # 关闭StanfordCoreNLP对象
# nlp.close()


# from stanfordcorenlp import StanfordCoreNLP
# # 创建StanfordCoreNLP对象，指定Stanford CoreNLP工具包的路径和语言为中文
# nlp = StanfordCoreNLP(r"C:\Users\coc\Desktop\stanford-corenlp-full-2018-10-05", lang="zh")
print("对于任何一个句子，给出句法分析的结果:")
# 示例中文句子
sample_sentence_chinese = "小明硕士毕业于中国科学院计算所，后在日本京都大学深造。小明是一个很聪明的学生。"
# 使用Stanford CoreNLP的句法分析工具对中文句子进行句法分析
syntax_analysis_result = nlp.parse(sample_sentence_chinese)
# 打印句法分析结果
print(syntax_analysis_result)
# 关闭StanfordCoreNLP对象
nlp.close()
