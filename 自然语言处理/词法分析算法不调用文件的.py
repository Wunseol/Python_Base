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
def D_RECOGNIZE(tape, machine):
    index = 0
    current_state = machine["initial_state"]

    while True:
        if index == len(tape):
            if current_state in machine["accept_states"]:
                return "accept"
            else:
                return "reject"
            
        elif (current_state,tape[index],) not in machine["transition_table"]:
            return "reject"
        else:
            current_state = machine["transition_table"][(current_state, tape[index])]
            index += 1


# 示例用法：
# 定义一个状态机
state_machine = {
    "initial_state": "q0",
    "accept_states": ["q6"],
    "transition_table": {
        ("q0", "形"): "q1",
        ("q1", "式"): "q2",
        ("q2", "大"): "q3",
        ("q3", "于"): "q4",
        ("q4", "内"): "q5",
        ("q5", "容"): "q6",
    }
}

# 测试输入串
input_tape = "形式大于内容"
print(len(input_tape))
# 调用D_RECOGNIZE函数
result = D_RECOGNIZE(input_tape, state_machine)

# 输出结果
print(result)

