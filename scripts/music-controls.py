#!/usr/bin/python3

import sys
import os


def check_playing():
    x = os.system('mpc status')
    print('result', x)


def main():
    command = str(sys.argv[1]) 
    if command == 'play':
        pass


if __name__ == '__main__':
    check_playing()
    main()
