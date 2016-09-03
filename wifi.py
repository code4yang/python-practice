"""
登陆验证到wifi。
"""
import requests


def function(username='303', password='080019',url=r'http://192.168.1.254:8080/proauth/Msg', sid='3232235867', fun_name='ncWebInternetLogin', eng_flag='0'):
    session = requests.Session()
    data = {
        'username':username,
        'password':password,
        'sid':sid,
        'FunName':fun_name,
        'eng_flag':eng_flag
    }
    resp = session.post(url,data=data)

if __name__=='__main__':
    function()
