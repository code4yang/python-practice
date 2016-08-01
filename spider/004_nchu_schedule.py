import requests
from bs4 import BeautifulSoup

# 应对反爬虫，加上head信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'
                  ' (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36',
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}

# 请求参数
data = {"__EVENTTARGET": "", "__EVENTARGUMENT": "",
        "__VIEWSTATE": "%2FwEPDwUJNTY0MzMxNzM3D2QWBGYPZBYEAgMPDxYEHgdFbmFibGVk"
                       "aB4HVmlzaWJsZWhkZAIFDxYCHgVzdHlsZQUNZGlzcGxheTpub25lO2"
                       "QCAQ8WAh8CBSliYWNrZ3JvdW5kLWltYWdlOnVybCgvQXBwSW1hZ2Vz"
                       "L2p3Yy5qcGcpOxYCAgEPZBYEAgQPFgIeCWlubmVyaHRtbAUwIC0g5o"
                       "Ko5q2j5Zyo55m75b2VJnF1b3Q75pWZ5Yqh566h55CG57O757ufJnF1"
                       "b3Q7ZAIMDxAPZBYCHghvbmNoYW5nZQUQVXNlclR5cGVDaGFuZ2UoKR"
                       "AVAwnmlZnogYzlt6UG5a2m55SfEuWFrOWFsemCrueuseeZu%2BW9lR"
                       "UDDEBuY2h1LmVkdS5jbhBAc3R1Lm5jaHUuZWR1LmNuCEV4Y2hhbmdl"
                       "FCsDA2dnZ2RkZOcdpPvT0XnvQSSGVtNKMurb9oR9wJ2ilHaA759Ti5"
                       "tW",
        "__VIEWSTATEGENERATOR": "CA0B0334",
        "__EVENTVALIDATION": "%2FwEdAAnjLawQJNt7DsyFWsdADi0IuUiP5PmHIhiKNLdeixxrROAGh"
                             "QWkJlPuNZl5JBCSVioqGgLJV0m0siKzkCBhn9Fh7ixyIk7cehzrzFMW"
                             "1kZASArZSm1WFzSQmS1DSf%2Fp%2BaYE3OC930PL0JShweUlLDoAVv8"
                             "1PVMCG58%2FvnI426EAvM34O%2FGfAV4V4n0wgFZHr3f6kqJyMlwWYN"
                             "4%2Bg1DHiQdOESeYOgiO%2FD9ricl7H2cSzQ%3D%3D",
        "__VIEWTARGET": "E09AA178CFBED5105469B8FE14E9B8D466921544",
        "TimeZone": "%2B818",
        "username": "13201516",
        "password": "Nchu080019",
        "usertype": "%40stu.nchu.edu.cn",
        "Button1": "%E7%99%BB+%E5%BD%95"}

# 登录的url
login_url = "https://passport.nchu.edu.cn/Default.aspx?SiteID=3&Timespan=2016-07-24+17%3a30%3a28&ReturnURL=http%3a%2f%"
"2fjwc-publish.jwc.nchu.edu.cn%3a80%2fjsxsd%2fxk%2fLoginToXk%3fmethod%3dsso&SignText=15d585d2b5395cc828756f07a52f6165"


def login(session, student_no, password):
    """
    登录到南昌航空大学教务处系统,使用POST请求
    :param session: 开启的session会话
    :param student_no: 学号
    :param password: 密码
    :return: 已登录的会话
    """


session = requests.session()
resp = session.post(login_url, data=data, verify=False)
soup = BeautifulSoup(resp.content.decode('utf-8'), "lxml")
print(soup)

