#!/usr/bin/env python
                                                                                   
import os                            
import sys             
from pwn import *  


## shellcode template. Well defined provided interface for debugging when writing your payload
context.terminal = ["tmux", "splitw", "-h"]
                                                                                   
## binary name here
binary_name = './binary-name-here'                     
gdb_command = ''

## setup debug binary
debug_name = binary_name[:-1] + 'x'
if not os.path.exists(debug_name):
    os.system("cp %s %s" % (binary_name, debug_name))


is_debug = False
## program options
if '--debug' in sys.argv:
    is_debug = True

if is_debug:
    p = process(debug_name)
    gdb.attach(p)
    raw_input("Press ENTER to continue to execute the program...")
else:
    p = process(binary_name)

global_random = p.elf.symbols['global_random']

print(hex(global_random))

## exploit here

p.recv()


payload = 
print(payload)

print(len(payload))


p.sendline(payload)


p.interactive()

