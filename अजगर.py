import sys
import copy
import os

mapping={
    "int":"संख्या",
    "def":"परिभाषा",
    "import":"आयात",
    "for":"के_लिये",
    "input":"इनपुट",
    "print":"छापो",
    "range":"पहुंच",
    "in":"में",
    "if":"अगर",
    "else":"अन्यथा",
    "elif":"या",
    "while":"जब_तक",
    "input ":"लो ",
}
def convertToEnglish(line):
    for key,value in mapping.items():
        line=line.replace(value,key)
    return line

def convertExceptionToEnglish(e):
        e=str(e)
        #for key,value in mapping.items():
        #    e=e.replace(key,value)
        print("चूक हुई है \n",e)


def exitFromProgram():
    sys.exit()

def getInputFile():
    inputFile=None
    if(len(sys.argv) <2):
        inputFile=input("Enter name of py file to execute\n")
    else:
        inputFile=sys.argv[1]
    return inputFile


def openFiles(inputFile,bufferFileName):
        try:
            fh=open(inputFile,"r",encoding="utf-8")
        except:
            print("Input file not found / could not be opened in read mode")
            exitFromProgram()
        try:
            fh_temp=open(bufferFileName,"w",encoding="utf-8")
        except:
            print("Please provide permission to write file")
            exitFromProgram()
        return fh, fh_temp

def closeFiles(fh,fh_temp):
    fh_temp.close()
    fh.close()

def convertAndWriteTo(inputFile,bufferFileName):
    fh,fh_temp=openFiles(inputFile,bufferFileName)
    for line in fh:
        fh_temp.write(convertToEnglish(line))
    closeFiles(fh,fh_temp)

def executeFile(fileName):
    exec(compile(open(fileName,encoding="utf-8").read(), fileName, 'exec'))


def executeFileAndPrint(bufferFile):
    try:
        executeFile(bufferFile)
    except Exception as e:
        convertExceptionToEnglish(e)


#main
inputFile=getInputFile()
bufferFile="temp.py"
convertAndWriteTo(inputFile,bufferFile)
executeFileAndPrint(bufferFile)	


print('Program Finished Execution')
