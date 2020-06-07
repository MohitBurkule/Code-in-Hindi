def countint(z):
    combi=[1]
    c=0
    for i in range(2,(z)):
        while(sum(combi)>z):
                combi.pop(0)
        if(sum(combi)<z):
            combi.append(i)
        elif(sum(combi)==z):
            #print(combi)
            c+=1
            combi.append(i)
        else:
            combi.pop(0)
    if(sum(combi)==z):
            c+=1
            #print(combi)
    print(c)
#6000000000000000000000000
