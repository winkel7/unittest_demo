# _*_ coding=utf-8 _*_
import os
import unittest
import requests
from unittestreport import ddt, list_data
from jsonpath import jsonpath

from common.handle_excel import HandleExcel
from common.handle_conf import cof
from common.handle_path import DATA_DIR
from common.handle_log import log
from common.tools import replace_data
from testcases.fixture import BaseTest


@ddt
class TestRecharge(unittest.TestCase, BaseTest):
    excel = HandleExcel(os.path.join(DATA_DIR, 'apicase.xlsx'), 'recharge')
    cases = excel.read_excel()

    @classmethod
    def setUpClass(cls):
        '''用例类的前置方法，提取token'''
        # 请求登录接口，进行登录
        cls.user_login()

    @list_data(cases)
    def test_recharge(self, item):
        # 第一步：准备请求数据
        # **********************动态替换参数*************************************
        # iterm['data'] = iterm['data'].replace("${member_id}", str(self.member_id))
        item['data'] = replace_data(item['data'], TestRecharge)
        # **********************************************************************
        url = cof.get('env', 'base_url') + item['url']
        method = item['method'].lower()
        params = eval(item['data'])
        expected = eval(item['expected'])
        # 第二步：发起请求，获取接口请求结果
        response = requests.request(method=method, url=url, json=params, headers=self.headers)
        res = response.json()
        print(res)
        # 第三步：断言
        try:
            self.assertEqual(expected['code'], res['code'])
            self.assertEqual(expected['msg'], res['msg'])
        except Exception as e:
            log.error(f"用例---【{item['title']}】---执行失败")
            raise e
        else:
            log.info(f"用例---【{item['title']}】---执行通过")
