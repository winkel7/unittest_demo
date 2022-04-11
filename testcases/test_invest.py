import os
import unittest

from jsonpath import jsonpath
import requests
from unittestreport import ddt, list_data

from common.handle_conf import cof
from common.handle_excel import HandleExcel
from common.handle_log import log
from common.handle_path import DATA_DIR
from testcases.fixture import BaseTest
from common.tools import replace_data


@ddt
class TestInvest(unittest.TestCase, BaseTest):
    excel = HandleExcel(os.path.join(DATA_DIR, 'apicase.xlsx'), 'invest')
    cases = excel.read_excel()

    @classmethod
    def setUpClass(cls) -> None:
        # 管理员登录
        cls.admin_login()
        # 普通用户登录
        cls.user_login()
        # 添加项目
        cls.add_project()
        # 审核项目
        cls.audit()

    @list_data(cases)
    def test_invest(self, item):
        url = cof.get('env', 'base_url') + item['url']
        method = item['method']
        item['data'] = replace_data(item['data'], TestInvest)
        params = eval(item['data'])
        expected = eval(item['expected'])
        response = requests.request(url=url, method=method, json=params, headers=self.headers)
        res = response.json()
        print('预期结果：', expected)
        print('实际结果：', res)
        try:
            self.assertEqual(expected['code'], res['code'])
            self.assertIn(expected['msg'], res['msg'])
        except AssertionError as e:
            log.error(f"用例---【{item['title']}】---执行失败")
            log.exception(e)
            raise e
        else:
            log.info(f"用例---【{item['title']}】---执行通过")
