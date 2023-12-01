path = 'C:\Windows\notepad.exe'
print(path)                      #字符\n被转义为换行符
# C:\Windows
# otepad.exe
path = r'C:\Windows\notepad.exe' #原始字符串，任何字符都不转义
print(path)
# C:\Windows\notepad.exe
