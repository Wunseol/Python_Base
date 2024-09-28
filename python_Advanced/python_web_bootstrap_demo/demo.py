import pymysql
import web
import hashlib


urls = (
    '/login.html','login',
    '/', 'index',
)

# 链接mysql demo

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


name = '碧波龙'
sql = "select displayname,jobs,lifedata from lol where races='%s'"%name
sqlData = sqlSelect(sql)
print(sqlData)
print('\n')
for t in sqlData:
    print("名称：%s,职业：%s,生命：%s"%(t[0],t[1],t[2]))


print("------查询user表------")
sql = "select username,name,money from user;"
sqlData = sqlSelect(sql)
for t in sqlData:
    print(t)

print("\n\n新增数据。。。\n\n") 
sql  = "insert into user(username,password,money,name) values('admin','E10ADC3949BA59ABBE56E057F20F883E',200,'管理员');"
sqlWrite(sql)

print("\n------查询user表------")
sql = "select username,name,money from user;"
sqlData = sqlSelect(sql)
for t in sqlData:
    print(t)

render = web.template.render('templates/')
web.config.debug = False
app = web.application(urls, globals())
import tempfile
root = tempfile.mkdtemp()
store = web.session.DiskStore(root)
session = web.session.Session(app, store)
if __name__ == "__main__":
    app.run()


