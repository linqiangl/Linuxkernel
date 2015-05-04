import os
import re
 
## regex pattern for finding out the memory address range from the output line
pattern = re. compile (r'[\w|\d]+-[\w|\d]+')
with open ( '/proc/self/maps' , 'r' ) as file :
     for line in file :
         line = line.rstrip()
         if '[vdso]' in line:
             addr_range = pattern.findall(line)[ 0 ]
             start_addr, end_addr = [ int (addr, 16 )
                                     for addr in addr_range.split( '-' )]
 
fd = os. open ( '/proc/self/mem' , os.O_RDONLY)
os.lseek(fd, start_addr, os.SEEK_SET)
buf = os.read(fd, (end_addr - start_addr))
 
with open ( 'linux-gate.dso.1' , 'w' ) as file :
     file .write(buf)
     file .close()
os.close(fd)
