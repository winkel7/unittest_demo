import os.path
import unittest

from jsonpath import jsonpath
import requests
from unittestreport import ddt, list_data

from common.handle_conf import cof
from common.handle_excel import HandleExcel
from common.handle_log import log
from common.handle_path import DATA_DIR
from common.tools import replace_data
from testcases.fixture import BaseTest


@ddt
class TestAdd(unittest.TestCase, BaseTest):
    excel = HandleExcel(os.path.join(DATA_DIR, 'apicase.xlsx'), 'add')
    data = excel.read_excel()

    @classmethod
    def setUpClass(cls) -> None:
        '''前置登录，提取token'''
        cls.user_login()

    @list_data(data)
    def test_add(self, item):
        url = cof.get('env', 'base_url') + item['url']
        item['data'] = replace_data(item['data'], TestAdd)
        params = eval(item['data'])
        expected = eval(item['expected'])
        method = item['method']
        response = requests.request(method=method, url=url, json=params, headers=self.headers)
        res = response.json()
        print('预期结果：', expected)
        print('实际结果：', res)
        try:
            self.assertEqual(expected['code'], res['code'])
            self.assertEqual(expected['msg'], res['msg'])
        except Exception as e:
            log.error(f"用例---【{item['title']}】---执行失败")
            log.exception(e)
            raise e
        else:
            log.info(f"用例---【{item['title']}】---执行通过")
