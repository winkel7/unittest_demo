import yaml


def read_yaml():
    with open(file='./yaml.yaml', mode='r', encoding='utf-8') as f:
        data = yaml.load(f, yaml.Loader)
    return data


def write_yaml(data):
    with open(file='./yaml.yaml', mode='a', encoding='utf-8') as f:
        yaml.dump(data=data, stream=f, allow_unicode=True)


def clear_yaml():
    with open(file='./yaml.yaml', mode='w', encoding='utf-8') as f:
        f.truncate()
