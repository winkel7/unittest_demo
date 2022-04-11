import logging
import os
import time

from common.handle_conf import cof
from common.handle_path import LOG_DIR


def logger(name, filename, level, sh_level, fh_level):
    """
    日志生成器
    :param name: 操作人
    :param filename: 日志保存文件路径
    :param level: 日志收集器等级
    :param sh_level: 控制台输出器日志等级
    :param fh_level: 文件输出器日志等级
    :return: 返回日志器
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    sh = logging.StreamHandler()
    sh.setLevel(sh_level)
    logger.addHandler(sh)
    fh = logging.FileHandler(filename, encoding='utf-8')
    fh.setLevel(fh_level)
    logger.addHandler(fh)
    fmt = '[%(name)s: %(asctime)s] %(filename)s:%(lineno)d-%(levelname)s: [%(funcName)s] %(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)
    sh.setFormatter(formatter)
    return logger


log_name = time.strftime('%Y%m%d', time.localtime())
log = logger(name=cof.get('log_config', 'name'),
          filename=os.path.join(LOG_DIR, f'{log_name}.log'),
          level=cof.get('log_config', 'level'),
          sh_level=cof.get('log_config', 'level'),
          fh_level=cof.get('log_config', 'level'))