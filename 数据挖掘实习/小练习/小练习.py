# 用python实现文档的处理，要求：
# 去掉有“>”号的这一行数据
# 针对有A,C,T,G字母的数据，在每一个字母中间添加空格
# 写入新文本。


# 一个with语句的开头。在Python中，with语句通常用于简化资源管理，确保在执行完特定代码块后能够正确关闭或释放资源，
# 即便在处理过程中出现异常也能确保资源得到妥善处理。这里是一个基本的使用示例：

# # 打开一个文件并自动关闭
# with open('example.txt', 'r') as file:
#     # 在此代码块内，file是打开的文件对象
#     content = file.read()
#     # 当离开这个with代码块时，不论是否发生异常，文件都会被自动关闭



# 打开输入和输出文件
with open('Python\数据挖掘实习\小练习\data.txt', 'r') as in_file, open('output_data.txt', 'w') as out_file:

    # 遍历输入文件的每一行
    for line in in_file:
        
        # 去掉包含 ">" 的行
        if '>' not in line:

            # 对于包含 A,C,T,G 的行，在每个字母间添加空格
            if set(['A', 'C', 'T', 'G']).intersection(line.upper()):
                # 将行转换为大写并去掉换行符
                processed_line = ''.join(line.replace('\n', '').upper())
                # 使用字符串替换方法在特定字母后面直接添加空格
                processed_line_with_spaces = processed_line.replace('A', 'A ').replace('C', 'C ').replace('T', 'T ').replace('G', 'G ')
                # 写入处理后的行到输出文件，并在末尾添加换行符
                out_file.write(processed_line_with_spaces + '\n')

            else:
                # 如果该行不包含 A,C,T,G，则原样写入（如果需要的话）
                out_file.write(line)

# 关闭输入和输出文件（由于使用了with语句，这里实际上不需要手动关闭）
                
