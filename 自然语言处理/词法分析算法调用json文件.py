# function D-RECOGNIZE(tape, machine)returns accept or reject
#     index <- Beginning of tape
#     current-state <- Initial state of machine
#     loop
#         if End of input has been reached then
#             if current-state is an accept state then
#                 return accept
#             else
#                 return reject
#         elsif transition-table[current-state , tape[index]] is empty then
#             return relect
#         else
#             current-state <- transition-table[current-state, tape[index]]
#             index<-index + 1
#     end 


import json
def fsm_recognize(word, rules):
    current_state = rules['start']
    for char in word:
        if char in rules['transitions'][current_state]:
            current_state = rules['transitions'][current_state][char]
        else:
            return False
    return current_state in rules['accept']

# 读取规则文件
with open(r'Python\自然语言处理\rules.json',encoding="utf-8") as f:
    rules = json.load(f)

# 词的识别
word = input('请输入要识别的词：')
if fsm_recognize(word, rules):
    print('识别成功！')
else:
    print('识别失败！')





