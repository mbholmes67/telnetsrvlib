#!/usr/bin/env python3

'''
Utility to read in the cmds.orig.py file, parse variable/values/comments, and export into a new format
'''

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parse the "cmds" telnetsrvlib')
    parser.add_argument('file', nargs=1, help='Filename to parse')
    args = parser.parse_args()
    file = args.file[0]

    with open(file, 'rt') as fp:
        lines = fp.readlines()
        for line in lines:
            items = line.strip().split('#')
            if items[0] == '':
                if len(items) == 1:
                    print()
                else:
                    print('# {}'.format(items[1]))
                continue
            else:
                exp_str = items[0]
                comment = None
                if len(items) >= 2:
                    comment = items[1]
            var_str, cmd_str = exp_str.split('=')
            num_str = cmd_str[cmd_str.find('(') + 1: cmd_str.rfind(')')]
            # out_str = '{:<20} = chr({:>3})'.format(var_str, num_str)
            out_str = '{:<20} = bytes([{:>3}])'.format(var_str, num_str)
            if comment is not None:
                out_str = '{}  #  {}'.format(out_str, comment)
            print(out_str)

