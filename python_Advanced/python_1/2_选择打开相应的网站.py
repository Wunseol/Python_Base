import webbrowser
choose =input ("Please reply to the page you want to open . \n1.shopping\n2.study\n3.buy a ticket\n4.travel\n")
if choose =="1":
    url= "http://www.jd.com"
elif choose =="2" :
    url= "http://sspu.fanya.chaoxing.com/portal"
elif choose =="3":
    url = "http://www.12306.com"
elif choose =="4":
    url = "http://www.ctrip.com"
webbrowser.open(url)