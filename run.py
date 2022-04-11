import os
import time
import unittest
import unittestreport
from common.handle_path import CASE_DIR, REPORT_DIR

suite = unittest.defaultTestLoader.discover(CASE_DIR)

report_name = time.strftime('%Y%m%d%H%M%S', time.localtime())+'.html'
filename = os.path.join(REPORT_DIR, report_name)
runner = unittestreport.TestRunner(suite, filename=filename, tester='winkel7')
runner.run()
