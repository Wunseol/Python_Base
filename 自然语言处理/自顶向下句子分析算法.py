# function ToP-DOWN-PARSE(input, grammar) returns a parse tree
#     agenda <-(Initial S tree, Beginning ofinput)
#     current-search-state <- POP(agenda)
#     loop
#         if SuCCESSFUL-PARSE?(current-search-state) then
#             return TREE(current-search-state)
#         else
#             if CAT(NODE-TO-EXPAND(current-search-state))is a POS then
#                 if CAT(node-to-expand)
#                     POS(CURRENT-INPUT(current-search-state))then
#                     PUSH(APPLY-LEXICAL-RULE(current-search-state),agenda)
#                     else
#                 return reject
#             else
#                 PUSH(APPLY-RULES(current-search-state, grammar),agenda)
#         if agenda is empty then
#             return reject
#         else
#             current-search-statet- NEXT(agenda)
#     end


class ParseTreeNode:
    def __init__(self, category, children=None):
        self.category = category
        self.children = children if children is not None else []

    def __str__(self, level=0):
        indent = "  " * level
        tree_str = f"{indent}({self.category}\n"
        for child in self.children:
            if isinstance(child, ParseTreeNode):
                tree_str += child.__str__(level + 1)
            else:
                tree_str += f"  {indent} {child}\n"
        tree_str += f"{indent})"
        return tree_str

def successful_parse(current_search_state):
    return current_search_state[1] == len(current_search_state[0].children)

def apply_lexical_rule(current_search_state):
    node_to_expand = current_search_state[0].children[current_search_state[1]]
    current_input = current_search_state[2]

    if node_to_expand == current_input:
        new_node = ParseTreeNode(node_to_expand)
        new_state = (current_search_state[0], current_search_state[1] + 1, current_search_state[2:])
        new_state[0].children.append(new_node)
        return new_state
    else:
        return None  # 拒绝，无法匹配输入

def apply_rules(current_search_state, grammar):
    node_to_expand = current_search_state[0].children[current_search_state[1]]
    applicable_rules = grammar.get_applicable_rules(node_to_expand)

    new_states = []
    for rule in applicable_rules:
        new_node = ParseTreeNode(rule[0], children=[rule[1]])
        new_tree = ParseTreeNode(current_search_state[0].category, children=current_search_state[0].children[:current_search_state[1]] + [new_node])
        new_state = (new_tree, current_search_state[1] + 1, current_search_state[2])
        new_states.append(new_state)

    return new_states

def next_state(agenda):
    return agenda.pop()

class Grammar:
    def __init__(self):
        # 根据具体的语法规则定义
        self.rules = {
            "S": [("NP", "VP")],
            "NP": ["The", "cat", "mat"],
            "VP": ["is", "on"]
        }

    def get_applicable_rules(self, category):
        return self.rules.get(category, [])

def to_top_down_parse(input_sequence, grammar):
    initial_state = (ParseTreeNode("S"), 0, input_sequence)
    agenda = [initial_state]

    while agenda:
        current_search_state = next_state(agenda)

        if successful_parse(current_search_state):
            return current_search_state[0]

        node_to_expand = current_search_state[0].children[current_search_state[1]]

        if isinstance(node_to_expand, str):  # 如果是终结符（POS）
            lexical_result = apply_lexical_rule(current_search_state)
            if lexical_result:
                agenda.append(lexical_result)
            else:
                return None  # 拒绝，无法匹配输入

        else:  # 如果是非终结符
            rules_result = apply_rules(current_search_state, grammar)
            agenda.extend(rules_result)

    return None  # 拒绝，agenda为空


# 示例用法
input_sequence = ["The", "cat", "is", "on", "the", "mat"]
grammar_rules = Grammar()
result_tree = to_top_down_parse(input_sequence, grammar_rules)

if result_tree:
    print("成功解析：")
    print(result_tree)

else:
    print("解析失败")
