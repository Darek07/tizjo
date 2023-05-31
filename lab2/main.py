#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    len_format = False
    for idx in range(0,len(format_string)):
        if shouldDo:
            len_format, length = is_length_format(format_string, idx)
            if format_string[idx] == '#' and (format_string[idx+1] == 'k' or len_format == True):
                if len_format == True:
                    param = param[:length]
                sw_cs = param.swapcase()
                print(sw_cs,end="")
                shouldDo=False
            else:
                print(format_string[idx],end="")
        else:
            if len_format and (format_string[idx] == '.' or is_digit(format_string[idx])):
                continue
            shouldDo=True
    print("")
    
def is_length_format(format_string, index):
    if not (format_string[index] == '#' and format_string[index+1] == '.'):
        return False, 0
    number = ''
    #print()
    for idx in range(index+2, len(format_string)):
        #print(format_string[idx])
        if is_digit(format_string[idx]):
            number += format_string[idx]
        elif format_string[idx] == 'k':
            return True, int(number)
        else: return False, number
        
def is_digit(c):
    return c in '0123456789'
        

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
