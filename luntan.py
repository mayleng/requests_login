#coding=utf-8
import requests
import re

#通过request模块发送get和post请求

#登录的url
login_url ="http://192.168.0.137:9007/Account/Login"
datas={
	"UserName":'may',
    "Password":'a123456'
}

Headers={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': '***',
    'Referer': 'http://192.168.0.137:9007/',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }

# 创建 session 对象。这个对象会保存所有的登录会话请求。
session_request = requests.session()

#提取在登录时所使用的 csrf标记
r=session_request.get(login_url,headers=Headers)
reg=r'<input name="__RequestVerificationToken" type="hidden" value=".*" />'
pattern = re.compile(reg)
ss = pattern.findall(r.text)
token = ss[0].split(" ")[3][7:][:-1]

#将token添加到datas中
#不同的网站可能设置不同的key值，通过浏览器开发者工具查看key值
datas['__RequestVerificationToken']=token



# 登录
result = session_request.post(
	login_url,
	data=datas,
	headers=Headers
	)

login_code=result.status_code
print("登录状态码："+str(login_code))


#发帖
#登录成功后发帖的网站
url = 'http://192.168.0.137:9007/'
#访问该网站，开始发帖   requests模块会自动管理session
tiezi = session_request.get(url,headers=Headers)

#网站源码挂了……后续下次接着写