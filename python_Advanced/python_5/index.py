#coding=utf-8

# 导入calendar模块，用于生成日历相关数据
import calendar
# 导入requests库，用于发送HTTP请求和获取网页资源
import requests
import web

# 定义URL路由，映射网站的不同页面路径到对应的处理类
# 这是Web应用的基础配置，决定了访问特定路径时应展示的内容
urls = (
    '/', 'index',  # 根路径 '/' 映射到 'index' 类，通常是网站首页
    '/calendar.html', 'rili',  # '/calendar.html' 路径映射到 'rili' 类，预计展示日历页面
    '/fanyi.html', 'fanyi',  # '/fanyi.html' 路径映射到 'fanyi' 类，预计提供翻译功能的页面
    '/resume.html', 'resume',  # '/resume.html' 路径映射到 'resume' 类，可能是展示简历或自我介绍的页面
)



# 定义一个处理主页请求的类
class index:
    # 定义响应GET请求的方法
    def GET(self):
        # 返回主页模板
        return render.index()

# 定义一个处理简历页面请求的类
class resume:
    # 定义响应GET请求的方法
    def GET(self):
        # 返回简历页面模板
        return render.resume()

# 定义一个处理日历页面请求的类
class rili:
    # 定义响应GET请求的方法
    def GET(self):
        # 返回指定年月的日历页面模板
        return render.calendarWeb("2022", "10", calendar.month(2022, 10))
    
    # 定义响应POST请求的方法
    def POST(self):
        # 获取表单提交的数据
        webData = web.input()
        # 从表单数据中获取年份，默认为"2022"
        year = webData.get("yearInput", "2022")
        # 从表单数据中获取月份，默认为"2022"
        month = webData.get("monthInput", "2022")
        # 根据获取的年份和月份生成日历数据
        data = calendar.month(int(year), int(month))
        # 返回生成的日历页面模板，包含年份、月份和日历数据
        return render.calendarWeb(year, month, data)

class fanyi:
    """
    翻译功能类，处理翻译查询和展示结果
    """
    
    def GET(self):
        """
        处理GET请求，返回翻译页面和默认示例
        
        返回:
        - 渲染后的翻译页面，包含默认查询词和解释列表
        """
        # 默认查询词
        q = "translate"
        # 默认解释列表
        explainList = [
            [1, "v. 翻译;译;被翻译;被译成;(使)转变，变为;（以某种方式）理解"],
        ]
        return render.fanyi(q, explainList)
        
    def POST(self):
        """
        处理POST请求，查询翻译内容并返回结果页面
        
        返回:
        - 渲染后的翻译页面，包含查询词和相应的解释列表
        """
        # 获取网页输入数据
        webData = web.input()
        # 获取查询词
        q = webData.get("q")
        # 构造有道翻译查询URL
        url = "https://dict.youdao.com/suggest?num=5&ver=3.0&doctype=json&cache=false&le=en&q=" + q
        # 发送GET请求获取翻译数据
        response = requests.get(url)
        # 解析响应为JSON格式数据
        data = response.json()

        # 初始化解释列表
        explainList = []
        # 遍历查询结果，提取解释内容
        i = 1
        for t in data["data"]["entries"]:
            # 将解释内容添加到列表
            explainList.append([i, t["explain"]])
            i += 1
        # 返回渲染后的翻译页面
        return render.fanyi(q, explainList)

# 初始化模板引擎，指定模板文件夹路径
render = web.template.render(r'C:\VS Code\Python\python_Advanced\python_5\templates/')

# 当此脚本作为主程序运行时
if __name__ == "__main__":
    # 创建Web应用对象
    app = web.application(urls, globals())
    # 运行Web应用
    app.run()