from yaml import dump
from yaml import safe_load as load



def read_config():
    with open('config.yaml', 'r') as f:
        return load(f)


def write_config(c):
    with open('config.yaml', 'w') as f:
        dump(c, f)

