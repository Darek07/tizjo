#!/usr/bin/env python3

import sys
import re

def sub_each_digit(param):
    replacements = {
        '-': '-',
        '1': '0',
        '2': '1',
        '3': '2',
        '4': '3',
        '5': '4',
        '6': '5',
        '7': '6',
        '8': '7',
        '9': '8',
        '0': '9'
    }

    res_array = [replacements[c] for c in str(param)]
    res = ''.join(res_array)
    
    return res


def my_printf(format_string,param):
    match = re.search(r'#(\d+)g', format_string)

    if not match:
        print(format_string)
        return

    r = match.group(0)
    param = sub_each_digit(param)

    first = match.group(1)
    if first:
        free_chars = int(first) - len(param)
        param = " " * max(0, free_chars) + param

    res = format_string.replace(r, param)
    print(res)

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
