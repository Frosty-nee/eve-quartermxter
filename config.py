from yaml import dump
from yaml import safe_load as load



def read():
    with open('config.yaml', 'r') as f:
        return load(f)


def write():
    with open('config.yaml', 'w') as f:
        dump(config, f)


config = read()

if __name__ == '__main__':
    pass
