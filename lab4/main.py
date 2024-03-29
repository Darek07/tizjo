#!/usr/bin/env python3

import sys
import re

def reverse_num(param):
    num = abs(int(param))
    no_zeros = str(num).rstrip('0') if num != 0 else str(num)
    return no_zeros[::-1]


def add_sign_if_appears(param):
    return '-' if int(param) < 0 else ''


def my_printf(format_string, param):
    match = re.search('#g', format_string)

    if not match:
        print(format_string)
        return

    replacement = match.group(0)
    try:
        param = add_sign_if_appears(param) + reverse_num(param)
    except ValueError:
        param = param

    print(format_string.replace(replacement, param))

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
