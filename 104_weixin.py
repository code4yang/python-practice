import xml.etree.cElementTree as ET
import time

ALLOWED_MSG_TYPES = set(['text', 'image', 'voice', 'video', 'shortvideo', 'location', 'link'])

ALLOWED_EVENTS = set(['subscribe', 'unsubscribe', 'unsub_scan',
                      'scan', 'click', 'location', 'view',
                      'templatesendjobfinish'])
a = """
<xml><ToUserName><![CDATA[gh_98d1cfbca9cb]]></ToUserName>
<FromUserName><![CDATA[ohel5v4DQI4515oQ0GR5Ck0bTFhg]]></FromUserName>
<CreateTime>1466730371</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[test]]></Content>
<MsgId>6299558975946964900</MsgId>
</xml>
"""

resp = """
<xml>
<ToUserName><![CDATA[{0}]]></ToUserName>
<FromUserName><![CDATA[{1}]]></FromUserName>
<CreateTime>{2}</CreateTime>
<MsgType><![CDATA[{3}]]></MsgType>
<Content><![CDATA[{4}]]></Content>
</xml>
"""
tree = ET.fromstring(a)
print(tree.find('Content').text)

a = ET.Element('root')
a.text = '<a>sdf</a>'
print(a.tag)
print(a.text)

b = ET.Element('b')
print(b.text)
print(b.tag)
a = u'\u4e2d\u6587'
r = resp.format('touser', 'fromuser', 'createtime', 'msgtype', a)
t = time.time().__int__()
print(t)
print(r)
