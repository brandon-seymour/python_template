import argparse

def get():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version', dest='version', default='1', help='Version')
    parser.add_argument('-s', dest='save', action='store_true', default=False, help="Default true")
    return parser.parse_args()