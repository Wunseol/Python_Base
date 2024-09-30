#coding=utf-8
import web
import pymysql
import hashlib
import tempfile

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

urls = (
    '/','organism',
)

class organism:
    def GET(self):
        query = "HCHO"
        sql = "select * from organism where name='%s' or formula = '%s'"%(query,query) 
        data =sqlSelect(sql)
        return render.organism(data)
    def POST(self):
        webData = web.input()
        query = webData.get("query")
        sql = "select * from organism where name='%s' or formula = '%s'"%(query,query) 
        data =sqlSelect(sql)
        print(data)
        return render.organism(data)
        

render = web.template.render(r'C:\VS Code\Python\python_Advanced\python_web_bootstrap_demo2\templates')
web.config.debug = False
app = web.application(urls, globals())
root = tempfile.mkdtemp()
store = web.session.DiskStore(root)
session = web.session.Session(app, store)
if __name__ == "__main__":
    app.run()
