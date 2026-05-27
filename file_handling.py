# File handling
# file=open('Sets.py')
# print(file.read())
# file.close()

"""
----
w-write       w mode file create karta hai and joh data ata hai usko overwrite karega 
a-append mode      
r-read mode      
x-create mode
"""


"""
file= open('Ironman.txt','w')
file.write('the content is now overwritten')
file.close()


file= open('Ironman.txt','a')
file.write(',the content is added using a.')
file.close()

 

file= open('Ironman.txt','r')
for i in file:
    print(i)
file.close()

"""

# with statment (auto close)
"""
with open('Ironman.txt','r') as file:
    print(file.read()) 

with open('Ironman.txt','w') as file:
    file.write('Content overwritten')
    print('DONE') 
    """


# paths
# C:\Users\HP\ZammanProject\Ironman.tx
"""
from pathlib import Path
p=Path('Ironman.txt')
if p.exists():
    print('file exists')
else:
    print('does not exists') """








