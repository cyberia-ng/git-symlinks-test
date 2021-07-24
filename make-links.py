#!/usr/bin/env python3

from sys import argv
from subprocess import run
from os import symlink


def main():
    target = argv[1]
    number_of_links = int(argv[2])
    src = target
    for link_num in range(number_of_links):
        dst = f'{target}-{link_num}'
        symlink(src, dst)
        src = dst


if __name__ == "__main__":
    main()
