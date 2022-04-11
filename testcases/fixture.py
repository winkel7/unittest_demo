import requests
from jsonpath import jsonpath

from common.handle_conf import cof


class BaseTest:

    @classmethod
    def admin_login(cls):
        url = cof.get('env', 'base_url') + '/member/login'
        # -------------管理员用户登录---------------------
        params = {
            "mobile_phone": cof.get('test_data', 'admin_mobile'),
            "pwd": cof.get('test_data', 'admin_pwd')
        }
        headers = eval(cof.get('env', 'headers'))
        response = requests.post(url=url, json=params, headers=headers)
        res = response.json()
        admin_token = jsonpath(res, '$..token')[0]
        headers['Authorization'] = 'Bearer ' + admin_token
        cls.admin_headers = headers
        cls.admin_member_id = jsonpath(res, '$..id')[0]

    @classmethod
    def user_login(cls):
        # ---------------普通用户登录---------------------------
        url = cof.get('env', 'base_url') + '/member/login'
        params = {
            "mobile_phone": cof.get('test_data', 'mobile'),
            "pwd": cof.get('test_data', 'pwd')
        }
        headers = eval(cof.get('env', 'headers'))
        # 发起登录请求
        response = requests.request(method='post', url=url, json=params, headers=headers)
        res = response.json()
        # 通过jsonpath获取token
        token = jsonpath(res, '$..[token]')[0]
        # 将token添加到请求头中
        headers['Authorization'] = 'Bearer ' + token
        # setattr(TestRecharge, 'headers', headers)
        cls.headers = headers
        # 获取上个请求的返回结果作为下个请求的入参
        cls.member_id = jsonpath(res, '$..id')[0]

    @classmethod
    def add_project(cls):
        # -------------添加项目-------------------------------
        url = cof.get('env', 'base_url') + '/loan/add'
        params = {
            "member_id": cls.member_id,
            "title": "借钱实现财务自由",
            "amount": 2000,
            'loan_rate': 18.0,
            "loan_term": 3,
            "loan_date_type": 1,
            "bidding_days": 5
        }
        response = requests.post(url=url, json=params, headers=cls.headers)
        res = response.json()
        cls.loan_id = jsonpath(res, '$..id')[0]

    @classmethod
    def audit(cls):
        """审核"""
        url = cof.get('env', 'base_url') + '/loan/audit'
        params = {"loan_id": cls.loan_id,
                  "approved_or_not": "true"
                  }
        requests.patch(url=url, json=params, headers=cls.admin_headers)
