import os
import random
import unittest

import requests
from unittestreport import ddt, list_data
from common.handle_path import DATA_DIR
from common.handle_excel import HandleExcel
from common.handle_log import log
from common.handle_conf import cof
from common.tools import replace_data


@ddt
class TestRegister(unittest.TestCase):
    excel = HandleExcel(os.path.join(DATA_DIR, 'apicase.xlsx'), 'register')
    cases = excel.read_excel()
    base_url = cof.get('env', 'base_url')
    headers = eval(cof.get('env', 'headers'))

    @list_data(cases)
    def test_register(self, item):
        # 第一步准备测试数据
        url = self.base_url + item['url']
        method = item['method'].lower()

        if '#mobile_phone#' in item['data']:
            TestRegister.mobile_phone = self.random_mobile()
            params = eval(replace_data(item['data'], TestRegister))
        else:
            params = eval(item['data'])
        expected = eval(item['expected'])

        response = requests.request(method=method, url=url, json=params, headers=self.headers)
        res = response.json()
        try:
            self.assertEqual(res['code'], expected['code'])
            self.assertEqual(res['msg'], expected['msg'])
        except Exception as e:
            log.error(f"用例---【{item['title']}】---执行失败")
            log.error(e)
            raise e
        else:
            log.info(f"用例---【{item['title']}】---执行通过")

    def random_mobile(self):
        return random.randint(13700000000, 13799999999)
