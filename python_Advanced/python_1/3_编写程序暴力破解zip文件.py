import zipfile
zFile=zipfile.ZipFile("Python\python_Practice\python_1\secret.zip")
passwd=0
while 1:
    try:
        try_passwd=str(passwd).encode("utf-8")
        zFile.extractall(pwd=try_passwd)
        print("password is %s"%try_passwd)
        break
    except:
        passwd=passwd+1
