#!/usr/bin/env python3

import sys
import re

def my_printf(format_string,param):
    match = re.search(r'#([1-9]\d*)?(\.\d+)?k', format_string)

    if not match:
        print(format_string)
        return

    sp = param.swapcase()
    r = match.group(0)

    second = match.group(2)
    if second:
        sp = sp[:int(second[1:])]
        
        
    first = match.group(1)
    if first:
        free_chars = int(first) - len(sp)
        sp = " " * max(0, free_chars) + sp

    res = format_string.replace(r, sp)
    print(res)
        

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
