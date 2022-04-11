import os

# 目录基本路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 日志文件路径
LOG_DIR = os.path.join(BASE_DIR, 'logs')

# 数据文件路径
DATA_DIR = os.path.join(BASE_DIR, 'datas')

# 配置文件路径
CONF_DIR = os.path.join(BASE_DIR, 'conf')

# 报告文件路径
REPORT_DIR = os.path.join(BASE_DIR, 'reports')

# 用例文件路径
CASE_DIR = os.path.join(BASE_DIR, 'testcases')