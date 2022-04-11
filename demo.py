import requests

# # 注册接口
# url = 'http://api.lemonban.com/futureloan/member/register'
# json = {'mobile_phone': '13576746524', 'pwd': '12345678', 'type': 0, 'reg_name': 'winkel'}
# header = {'X-Lemonban-Media-Type': 'lemonban.v1'}
# res = requests.post(url=url, json=json, headers=header)
# print(res.text)
#
# # 登录接口
# url = 'http://api.lemonban.com/futureloan/member/login'
# json = {'mobile_phone': '13576746524', 'pwd': '12345678'}
# header = {'X-Lemonban-Media-Type': 'lemonban.v2'}
# res = requests.post(url=url, headers=header, json=json)
# print(res.json())
from jsonpath import jsonpath

data = {"code": 0, "msg": "0", "message": "0", "ttl": 1,
        "data": [{"show_unfollowed_msg": 0, "msg_notify": 1, "set_like": 0, "set_comment": 0, "set_at": 0, },
                 {"show_unfollowed_msg": 1, "msg_notify": 3, "set_like": 2, "set_comment": 1, "set_at": 1, }]}
print(jsonpath(data, '$.data[?(@.set_like>=0)]'))
