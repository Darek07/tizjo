#!/usr/bin/env python3

import sys
import re

def my_printf(format_string,param):
    match = re.search(r'#\.(\d+)g', format_string)

    if not match:
        print(format_string)
        return

    r = match.group(0)

    first = match.group(1)
    if first:
        free_chars = int(first) - len(param)
        param = " " * max(0, free_chars) + param

    res = format_string.replace(r, param)
    print(res)

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
