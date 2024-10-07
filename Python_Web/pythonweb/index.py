# coding=utf-8

# 导入所需的模块
import calendar
import requests
import web

# 定义URL路由
urls = (
    '/', 'index',
    '/rili.html', 'rili',
    '/fanyi.html', 'fanyi',
    '/resume.html', 'resume',
)

# 初始化模板引擎
render = web.template.render(r'C:\VS Code\Python\Python_Web\pythonweb\templates/')

# 定义处理主页请求的类
class index:
    def GET(self):
        return render.index()

# 定义处理简历页面请求的类
class resume:
    def GET(self):
        return render.resume()

# 定义处理日历页面请求的类
class rili:
    def GET(self):
        return render.rili("2022", "10", calendar.month(2022, 10))
    
    def POST(self):
        webData = web.input()
        year = webData.get("yearInput", "2022")
        month = webData.get("monthInput", "10")
        data = calendar.month(int(year), int(month))
        return render.rili(year, month, data)

# 定义处理翻译页面请求的类
class fanyi:
    def GET(self):
        q = "translate"
        explainList = [
            [1, "v. 翻译;译;被翻译;被译成;(使)转变，变为;（以某种方式）理解"],
        ]
        return render.fanyi(q, explainList)
        
    def POST(self):
        webData = web.input()
        q = webData.get("q")
        url = "https://dict.youdao.com/suggest?num=5&ver=3.0&doctype=json&cache=false&le=en&q=" + q
        response = requests.get(url)
        data = response.json()

        explainList = []
        i = 1
        for t in data["data"]["entries"]:
            explainList.append([i, t["explain"]])
            i += 1
        return render.fanyi(q, explainList)

# 当此脚本作为主程序运行时
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()


