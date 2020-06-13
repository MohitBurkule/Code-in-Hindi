import sys
import copy
import os
import re
import random
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

def extractDoubleQuoteStrings(line):
    dstrs=re.findall(r'\"(.*?)\"',line)
    dmap=dict()
    for dstr in dstrs:
        intId=random.randint(0,10000)
        id='__code_in_hindi_double_quotes'+str(intId)+'__'
        dmap[id]=dstr
        line=line.replace(dstr,id)
    return line,dmap


def extractSingleQuoteStrings(line):
    sstrs=re.findall(r"\'(.*?)\'",line)
    smap=dict()
    for sstr in sstrs:
        intId=random.randint(0,10000)
        id='__code_in_hindi_single_quotes'+str(intId)+'__'
        smap[id]=sstr
        line=line.replace(sstr,id)
    return line,smap

def restoreSingleQuoteStrings(line,smap):
    for id,sstr in smap.items():
        line=line.replace(id,sstr)
    return line
def restoreDoubleQuoteStrings(line,dmap):
    for id,dstr in dmap.items():
        line=line.replace(id,dstr)
    return line
def removeSingleLineComment(line):
    line=re.split(r'#[^\n]*',line)
    return ''.join(line)
def preprocessLine(line):
    line,dmap=extractDoubleQuoteStrings(line)
    line,smap=extractSingleQuoteStrings(line)
    line=removeSingleLineComment(line)
    string_handling_maps=[dmap,smap]
    return line,string_handling_maps

def postprocessLine(line,string_handling_maps):
    dmap=string_handling_maps[0]
    smap=string_handling_maps[1]
    line=restoreSingleQuoteStrings(line,smap)
    line=restoreDoubleQuoteStrings(line,dmap)
    return line

def convertLexemesToTarget(line):
    for key,value in mapping.items():
        line=line.replace(value,key)
    return line


def convertToEnglish(line):
    line,string_handling_maps=preprocessLine(line)
    line=convertLexemesToTarget(line)
    line=postprocessLine(line,string_handling_maps)

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
