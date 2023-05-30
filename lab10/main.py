#!/usr/bin/env python3

import sys
import re

def convert_num(num):
    # F=int((O*2)/N)
    O = abs(int(num))
    N = len(str(O))
    F = int((O * 2) / N)

    if F % 2 != 0:
        F = str(hex(F)).replace('0x', '')
    if int(num) < 0:
        F = -int(F)
    return str(F)


def my_printf(format_string,param):
    match = re.search(r'#a', format_string)

    if not match:
        print(format_string)
        return

    r = match.group(0)
    
    try:
        param = int(param)
    except Exception:
        param = 0

    converted = convert_num(param)
    
    res = format_string.replace(r, converted)
    print(res)

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
