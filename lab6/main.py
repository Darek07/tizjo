#!/usr/bin/env python3

import sys
import re


def add_start_zeros(param, num):
    str_param = str(abs(int(param)))
    zeros_len = max(0, num - len(str_param) - (1 if int(param) < 0 else 0))
    zeros = zeros_len * "0"
    return zeros + str_param


def convert(str_param):
    formula = lambda x: str((int(x) * 9 + 1) % 10)
    return ''.join([formula(digit) for digit in str_param])


def my_printf(format_string,param):
    match = re.search(r'#\.(\d+)g', format_string)

    if not match:
        print(format_string)
        return

    r = match.group(0)
    num = int(match.group(1))
    
    zero_param = add_start_zeros(param, num)
    converted_param = convert(zero_param)
    sign_param = ('-' if int(param) < 0 else '') + converted_param

    res = format_string.replace(r, sign_param)
    print(res)

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
