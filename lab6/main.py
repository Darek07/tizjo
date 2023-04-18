#!/usr/bin/env python3

import sys
import re

def add_start_zeros(param, num):
    str_param = str(abs(param))
    zeros_len = max(0, num - len(str_param))
    zeros = zeros_len * "0"
    return zeros + str_param

def convert(str_param):
    formula = lambda x: (int(x) * 9 + 1) % 10
    return ''.join([formula(digit) for digit in str_param])

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
