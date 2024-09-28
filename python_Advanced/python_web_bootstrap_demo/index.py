#coding=utf-8
import calendar
import hashlib

import pymysql
import requests
import web

urls=(
    '/login.html','login',
    '/', 'index',
    '/calendar.html','rili',
    '/fanyi.html','fanyi',
    '/resume.html','resume',
    '/lol.html', 'lol',

)

# 链接mysql

def sqlSelect(sql):
    conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='nhcwc',db='web')
    cur = conn.cursor()
    cur.execute(sql)
    sqlData=cur.fetchall()
    cur.close()
    conn.close()
    return sqlData

def sqlWrite(sql):
    conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='nhcwc',db='web')
    cur = conn.cursor()
    cur.execute(sql)
    cur.close()
    conn.commit()
    conn.close()
    return

# ok

class login:
    def GET(self):
        return render.login("")

    def POST(self):
        webData = web.input()
        username = webData.get("username")
        password = webData.get("password")
        #计算密码的md5值
        m = hashlib.md5()
        m.update(password.encode("utf-8"))
        password = m.hexdigest()

        sql = "select name from user where username ='%s' and password='%s'"%(username,password)
        sqlData = sqlSelect(sql)
        if len(sqlData)==0:
            return render.login("密码错误")
        else:
            session.username = username
            session.name = sqlData[0][0]
            print(session.name)
            raise web.seeother('/')

        
class index:
    def GET(self):
        print(session.get('name'))
        if session.get('name')==None:
            raise web.seeother('/login.html')
        else:
            return render.index(session.name)

        
class lol:
    def GET(self):
        notice = ""
        return render.lol("敖兴",['','','','','','',''],notice)

    def POST(self):

        webData = web.input()
        query = webData.get("query")

        sql = "select tftid,displayname,races,skillname,attackdata,lifedata,skillintroduce from lol where displayname='%s'"%query
        sqlData = sqlSelect(sql)
        
        if len(sqlData)==0:
            notice ="Not Found"
            sqlData = ['','','','','','','']
        else:
            notice = ""
            sqlData = sqlData[0]

        print(notice,sqlData)
        
        return render.lol(query,sqlData,notice)
    

class resume:
    def GET(self):
        return render.resume()
    
    
class rili:
    def GET(self):
        return render.riliWeb("2022","09",calendar.month(2022,9))
    
    def POST(self):
        webData = web.input()
        year = webData.get("yearInput","2022")
        month = webData.get("monthInput","10")
        data = calendar.month(int(year),int(month))
        return render.riliWeb(year,month,data)
  
    
class fanyi:
    def GET(self):
        q = "Python"
        explainList = [
            [1,"n. 巨蟒；大蟒；丹舌; n. （Python）人名；（法）皮东"],
            [2,"n. 蟒蛇（python 的复数）"],
            [3,"adj. 预言的；神谕的；大蟒似的"],
            [4,"n. 女预言家；女巫；古希腊德尔菲的太阳神殿的女祭司"],
            [5,"adj. 皮东风格的；搞笑的；奇怪的"]
        ]
        flag = 1
        return render.youdao(q,explainList,flag)
        
    def POST(self):
        webData = web.input()
        q = webData.get("q")
        if "search" in webData:
            url = "https://dict.youdao.com/suggest?num=5&ver=3.0&doctype=json&cache=false&le=en&q="+q
            response = requests.get(url)
            data = response.json()

            explainList = []
            i = 1
            s = ""
            for t in data["data"]["entries"]:
                explainList.append([i,t["explain"]])
                s += t["explain"]
                i+=1
            if s=="":
                s = "Fail"
            sql = "insert into history(username,query,result) values('%s','%s','%s')"%(session.username,q,s)
            sqlWrite(sql)
            flag =1
            return render.youdao(q,explainList,flag)
        else:
            sql = "select history.time,user.name,query,result from history,user where history.username=user.username"
            sqlData = sqlSelect(sql)
            flag = 0
            return render.youdao(q,sqlData,flag)


render = web.template.render(r'C:\VS Code\Python\python_Advanced\python_6\templates/')
web.config.debug = False
app = web.application(urls, globals())
import tempfile

root = tempfile.mkdtemp()
store = web.session.DiskStore(root)
session = web.session.Session(app, store)


if __name__ == "__main__":
    app.run()

