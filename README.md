# अजगर
अब, कोड लिखें  हिंदी में
( Python wrapper for hindi language  )

Exe in output folder 

#WHY?

Because there are many students who dont know proper english 
Hindi or any  local language is closer to them and they can understand code better if it is in their local language

#What is it ?

It is a wrapper around standard python which allows users to type the code in HINDI language 

#Usage

अजगर input_hindi.py

where 
1) अजगर 	is the exe in the output folder 
2) input_hindi.py is any hindi-python code file

example of input_hindi.py
```
###  जादूगर 	

कम  = 1
ज्यादा  = 1000

छापो(" १  से  १००० के बीच कोई भी एक संख्या दीजिए . मई आपका मन पढ़कर वो संख्या बताऊँगा , बस १० सवालों मई ")

## ये सवाल नो है 
सवाल_नो  = 1
जब_तक  कम  < ज्यादा :
    छापो (कम ,ज्यादा )
    ## you will realise that you need the "+1" below...
    बीच  = (कम  + ज्यादा )//2 + 1
    परिणाम  = input("%d: क्या आपकी संख्या  %d से कम हु (y/n)?" % (सवाल_नो , बीच ))
    अगर  परिणाम.छोटा ()[0] == 'y':
        ज्यादा  = बीच  -1
    अन्यथा :
        कम  = बीच 
    सवाल_नो = सवाल_नो + 1

छापो ("आपकी संख्या है :", कम)
```

#HOW does it work?

It simply has a mapping which converts hindi words to their corresponding english words and then runs python interpretor behind the scenes 	

#Issues
1) Only a few python keywords have their corresponding hindi word 
2) default packages and methods also need to be converted to hindi 
3) errors are still shown in english



	
