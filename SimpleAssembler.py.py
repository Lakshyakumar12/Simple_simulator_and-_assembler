import sys
dict=['add','10000','sub','10001','mul','10110','xor','11010','or','11011','and','11100','R1','001','R2','010','R3','011','R0','000','R4','100','R5','101','R6','110']
dict2=['mov','10011','div','10111','not','11101','cmp','11110','R1','001','R2','010','R3','011','R0','000','R4','100','R5','101','R6','110','FLAGS','111']
dict3=['ld','10100','001','st','10110','R1','001','R2','010','R3','011','R0','000','R4','100','R5','101','R6','110']
dict4=['R1','001','R2','010','R3','011','R0','000','R4','100','R5','101','R6','110','mov','10010','ls','110001','rs','11000']
dict5=['jmp','11111','jlt','01100','jgt','01101','je','01111']
#f = open("cc.txt", "r")
l = [[str(x) for x in line.split()] for line in sys.stdin]
l=list(filter(None,l))

o=[]
pp=[]
k=[]

uu=0
ee=0
for i in range(0,len(l)):
    if l[i][0]=="var":
        pp.append(l[i][1])
        pp.append(i)
        ee=ee+1
    else:
        break


for i in range(ee,len(l)):
    if l[i][0]!="var":



        p = l[i][0]
        if p[len(p) - 1] == ':':
            p=p.replace(":","")
            o.append(p)
            o.append(uu)
            l[i].pop(0)
        uu=uu+1




binary=[]
err=0

l=list(filter(None,l))

for i in range(ee,len(l)):
    if l[i][0]=="hlt":
        pass
    elif l[i][0]=="var":
        k.append("Error at line" + str(i + 1) + " variable declared in between ")
        err=1



    elif l[i][0] in dict:
        p = str()
        flag = 0
        if len(l[i])==4:
            for j in range(0, len(l[i])):
                if l[i][j] in dict:
                    ind = dict.index(l[i][j])
                    p = p + dict[ind + 1]

                    if flag == 0:
                        p = p + '00'
                    flag = 1
                else:
                    k.append("Error at line" + str(i + 1) + " wrong register value ")
                    err=1
            binary.append(p)
            p=""
        else:
            k.append("Error at line"+str(i+1)+"Incomplete command or register missing")
            err=1
    elif l[i][0] in dict4 and "$" in l[i][2]:

        if len(l[i])==3:
            p = str()

            for j in range(0, len(l[i])-1):
                if l[i][j] in dict4:
                    ind = dict4.index(l[i][j])
                    p = p + dict4[ind + 1]
                else:
                    k.append("Error at line" + str(i + 1) + "  wrong register value  ")
                    err = 1
            y=str(l[i][2])
            tt=y
            tt=tt.replace("$","")
            tt=int(tt)
            if "$" in y and (tt <=255 and tt>=0):
                y=y.replace("$","")
                u = bin(int(y)).replace("0b", "")

                u = str(u)
                t = 8 - len(u)
                for i in range(0, t):
                    u = '0' + u
                p = p + u
                binary.append(p)
                p = ""
            else:
                k.append("Error at line" + str(i + 1) + " IMM not in range or invalid imm syntax ")
                err=1
        else:
            k.append("Error at line" + str(i + 1) + " Incomplete command or register missing ")
            err=1
    elif l[i][0] in dict2:
        if len(l[i])==3:
            p = str()
            flag = 0
            for j in range(0, len(l[i])):
                if l[i][j] in dict2:
                    ind = dict2.index(l[i][j])
                    p = p + dict2[ind + 1]

                    if flag == 0:
                        p = p + '00000'
                    flag = 1
                else:
                    k.append("Error at line" + str(i + 1) + " wrong register value ")
                    err=1
            binary.append(p)
            p=""
        else:
            k.append("Error at line" + str(i + 1) + " Incomplete command or register missing ")
            err = 1
        if l[i][2]=='FLAGS' and l[i][0]!='mov':
            k.append("Error at line" + str(i + 1) + " Flag command can only be used with mov command ")
            err = 1

    elif l[i][0] in dict3:
        if len(l[i])==3:
            if l[i][2] in pp:
                p = str()
                flag = 0
                for j in range(0, len(l[i])-1):
                    if l[i][j] in dict3:
                        ind = dict3.index(l[i][j])
                        p = p + dict3[ind + 1]
                    else:
                        k.append("Error at line" + str(i + 1) + " wrong register value ")
                        err=1
                v=pp.index(l[i][2])
                v=pp[v+1]

                u = bin(i-ee+1).replace("0b", "")
                u = str(u)
                t = 8 - len(u)
                for i in range(0, t):
                    u = '0' + u
                p = p + u
            else:
                k.append("Error at line" + str(i + 1) + " variable not declared  ")
                err=1

            binary.append(p)
            p = ""
        else:
            k.append("Error at line" + str(i + 1) + " Incomplete command or register missing ")
            err = 1

    elif l[i][0] in dict5:
        if len(l[i])==2:
            if l[i][1] not in o:
                k.append("Error at line" + str(i + 1) + " label not declared ")
                err=1
            else:
                p=str()
                ind = dict5.index(l[i][0])
                p=p+dict5[ind + 1]
                p=p+"000"
                ind=o.index(l[i][1])
                u=o[ind+1]

                u = bin(u).replace("0b", "")
                t = 8 - len(u)
                for i in range(0, t):
                    u = '0' + u


                p=p+u
                binary.append(p)
                p = ""

        else:
            k.append("Error at line"+str(i+1)+" Invalid syntax ")
            err=1
    else:
        k.append("Error at line" + str(i + 1) + " Incomplete command or register missing ")
        err = 1
for i in range(0,len(l)-1):
    if l[i][0]=="hlt":
        k.append("Error at line"+str(i+1)+" hlt cmmnd cannot be used in between")
        err=1
if l[len(l)-1][0]!="hlt":
    k.append("Error at line" + str(len(l)) + " hlt cmmnd was no used in end")
    err=1

if err==0:
    for i in binary:
        print(i)
    print("0101000000000000")
else:
    for i in k:
        print(i)
