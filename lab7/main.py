#!/usr/bin/env python3

import sys
import re

def my_printf(format_string,param):
    match = re.search(r'#j', format_string)

    if not match:
        print(format_string)
        return

    r = match.group(0)
    hex_param = hex(param)
    
    res = format_string.replace(r, hex_param)
    print(res)

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
