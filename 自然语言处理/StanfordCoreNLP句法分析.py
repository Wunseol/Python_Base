from stanfordcorenlp import StanfordCoreNLP
# # 创建StanfordCoreNLP对象，指定Stanford CoreNLP工具包的路径和语言为中文
nlp = StanfordCoreNLP(r"C:\Users\coc\Desktop\stanford-corenlp-full-2018-10-05", lang="zh")
print("对于任何一个句子，给出句法分析的结果:")
# 示例中文句子
# 输入中文句子
print("例如：我喜欢吃饭，我喜欢睡觉，我喜欢打球。小明硕士毕业于中国科学院计算所，后在日本京都大学深造。小明是一个很聪明的学生。")
sample_sentence_chinese = input("请输入中文句子:")
print("")
print(sample_sentence_chinese)
print("")
# 使用Stanford CoreNLP的句法分析工具对中文句子进行句法分析
syntax_analysis_result = nlp.parse(sample_sentence_chinese)
# 打印句法分析结果
print(syntax_analysis_result)
# 关闭StanfordCoreNLP对象
nlp.close()


