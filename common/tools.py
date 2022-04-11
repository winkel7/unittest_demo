import re


def replace_data(data, cls):
    while re.search(r"#(.+?)#", data):
        res = re.search(r'#(.+?)#', data)
        item = res.group()
        attr = res.group(1)
        value = getattr(cls, attr)
        data = data.replace(item, str(value))
    return data

if __name__ == '__main__':
    class Test:
        id = 1
        name = 'zhangsan'
    data = 'id:#id#,name=#name#'
    res = replace_data(data,Test)
    print(res)