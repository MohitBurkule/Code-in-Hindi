import sys
import copy
import os

if(len(sys.argv) <2):
    print(" Need More than 2 Arguments ")
    exit()
mapping={
    "import":"आयात",
    "for":"के_लिये",
    "input":"इनपुट",
    "print":"छापो",
    "range":"पहुंच",
    "in":"में",
    "if":"अगर"}


fh=open(sys.argv[1],"r",encoding="utf-8")
fh_temp=open("temp.py","w",encoding="utf-8")
for line in fh:
    for key,value in mapping.items():
        line=line.replace(value,key)
    fh_temp.write(line)
fh_temp.close()
fh.close()
#execfile('file.py')
#os.system('python temp.py')
try:
    exec(compile(open('temp.py',encoding="utf-8").read(), 'temp.py', 'exec'))
except Exception as e:
    e=str(e)
    for key,value in mapping.items():
        e=e.replace(key,value)
    print("hi",e)


print('Program Finished Execution')
