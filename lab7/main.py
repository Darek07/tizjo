#!/usr/bin/env python3

import sys
import re

replacements = {
    'a': 'g',
    'b': 'h',
    'c': 'i',
    'd': 'j',
    'e': 'k',
    'f': 'l'
}

def my_printf(format_string,param):
    match = re.search(r'#j', format_string)

    if not match:
        print(format_string)
        return

    r = match.group(0)
    
    if param.startswith('0x'):
        hex_param = str(param)[2:]
    else:
        hex_param = str(hex(int(param)))[2:]

    replaced = ''.join([replacements[c] if c in replacements else c for c in hex_param.lower()])
    
    res = format_string.replace(r, replaced)
    print(res)

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
