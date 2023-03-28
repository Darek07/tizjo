#!/usr/bin/env python3

import sys
import re

def reverse_num(param):
    return str(abs(param))


def add_sign_if_appears(param):
    return '-' + str(param) if param < 0 else str(param)


def my_printf(format_string, param):
    match = re.search('#g', format_string)

    if not match:
        print(format_string)
        return

    replacement = match.group(0)
    param = add_sign_if_appears(param) + reverse_num(param)

    print(format_string.replace(replacement, param))

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
