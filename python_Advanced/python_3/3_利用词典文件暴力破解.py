# 3.	利用词典文件“dict.txt”暴力破解“secret2.zip”文件

import zipfile

zFile=zipfile.ZipFile("C:\\VS Code\\Python\\python实习\\python_3\\secret2.zip")

fob_j = open("C:\VS Code\Python\python实习\python_3\dict.txt","r")

for t2 in fob_j:
    passwd=t2.strip('\n')
    try:
        try_passwd=str(passwd).encode("utf-8")
        zFile.extractall(pwd=try_passwd)
        print("password is %s"%try_passwd)
        break
    except:
        pass

zFile.close()
fob_j.close()
