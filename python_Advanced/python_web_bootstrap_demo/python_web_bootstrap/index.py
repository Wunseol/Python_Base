#coding=utf-8
# 导入web模块，用于创建web应用程序
import web

# 定义URL路由，将根路径'/'映射到index类
urls = (
    '/', 'index',
)

# # 定义index类，处理根路径的GET请求
# class index:
#     # 定义GET方法，当收到GET请求时返回HTML内容
#     def GET(self):
#         # 返回一个简单的HTML内容，包含问候语和Python关键字
#         return "<h1>Hello, world!</h1><p> Python</p>"
    
class index:
    def GET(self):
        return render.index()


# 初始化模板渲染器，使用'templates/'目录下的模板文件
render = web.template.render(r'B:\VS Code\Python\python_Advanced\python_5\python_web_bootstrap/')

# 当模块作为主程序运行时，创建并启动web应用程序
if __name__ == "__main__":
    # 创建web应用程序实例，使用定义好的URL路由和全局变量
    app = web.application(urls, globals())
    # 运行web应用程序
    app.run()


