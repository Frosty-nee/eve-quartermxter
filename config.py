from yaml import dump
from yaml import safe_load as load



def read():
    with open('config.yaml', 'r') as f:
        return load(f)


def write():
    with open('config.yaml', 'w') as f:
        dump(config, f)

def update_from_file():
    for k,v in read().items():
        globals()[k] = v

update_from_file()


if __name__ == '__main__':
    pass
