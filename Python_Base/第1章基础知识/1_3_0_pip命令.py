

# pip download SomePackage[==version] 下载扩展库的指定版本，不安装

# pip freeze [> requirements.txt] 以requirements的格式列出已安装模块

# pip list 列出当前已安装的所有模块

# pip install SomePackage[==version] 在线安装SomePackage模块的指定版本

# pip install SomePackage.whl 通过whl文件离线安装扩展库

# pip install package1 package2 ... 依次（在线）安装package1、package2等扩展模块

# pip install -r requirements.txt 安装requirements.txt文件中指定的扩展库

# pip install --upgrade SomePackage 升级SomePackage模块

# pip uninstall SomePackage[==version] 卸载SomePackage模块的指定版本


# 在Windows平台上，如果在线安装扩展库失败，可以从http://www.lfd.uci.edu/~gohlke/pythonlibs/下载扩展库编译好的.whl文件（注意版本，并且一定不要修改下载的文件名），然后在命令提示符环境中使用pip命令进行离线安装。例如：

# pip install Django-2.1.3-py3-none-any.whl

# 如果由于网速问题导致在线安装速度过慢的话，pip命令还支持指定国内的站点来提高速度，下面的命令用来从阿里云下载安装扩展库jieba，其他服务器地址可以自行查阅。

# pip install jieba -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com

# 如果遇到类似于“拒绝访问”的出错信息，需要在执行pip命令时增加选项--user，例如

# pip install jieba --user



