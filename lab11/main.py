#!/usr/bin/env python3

import sys
import re

def convert(param):
    binary = bin(param)[2:]
    reversed_bin = binary[::-1]
    res = ''
    for i, bit in enumerate(reversed_bin):
        res += '0' if bit == '0' else 'abcdefghij'[i % 10]

    return res[::-1]


def my_printf(format_string, param):
    match = re.search(r'#b', format_string)

    if not match:
        print(format_string)
        return

    r = match.group(0)
    
    try:
        param = int(param)
    except Exception:
        param = 0

    converted = convert(param)
    
    res = format_string.replace(r, converted)
    print(res)


data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
