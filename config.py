from yaml import dump
from yaml import safe_load as load


def read():
    with open('config.yaml', 'r') as f:
        return load(f)


def write():
    with open('config.yaml', 'w') as f:
        d = {opt: globals()[opt] for opt in options}
        dump(d, f)

def update_from_file():
    r = read()
    for k,v in r.items():
        globals()[k] = v
    globals()['options'] = r.keys()


update_from_file()
