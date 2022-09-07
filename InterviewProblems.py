strinput = str()

strinput = input("Please enter the term")
# Basic Idea - find the brackets, evaluate each operation inside then repeat for outside
# Limitations I would've like to improve on:
#  - limited to single operation per operand - ideally would've expanded this
#  - Calculator cannot handle multiplying or dividing negative digits, ideally this would've been improved on

def devide(in_str):
    divpos = in_str.find("/")
    if divpos == -1:
        return in_str
    count_start = divpos -1
    while count_start > 0:
        if not in_str[count_start:divpos].isnumeric():
            break
        count_start -= 1
    count_end = divpos + 2
    while count_end <= len(in_str):
        if not in_str[divpos+1:count_end].isnumeric():
            count_end -= 1
            break
        count_end+= 1
    res = float(in_str[count_start:divpos])/float(in_str[divpos+1:count_end])
    newstr = in_str[0:count_start]+str(res)+ in_str[count_end:len(in_str)]
    return newstr



def product(in_str):
    divpos = in_str.find("*")
    if divpos == -1:
        return in_str
    count_start = divpos -1
    while count_start > 0:
        if not in_str[count_start:divpos].isnumeric():
            break
        count_start -= 1
    count_end = divpos + 2
    while count_end <= len(in_str):
        if not in_str[divpos+1:count_end].isnumeric():
            count_end -= 1
            break
        count_end+= 1
    res = float(in_str[count_start:divpos])*float(in_str[divpos+1:count_end])
    newstr = in_str[0:count_start]+str(res)+ in_str[count_end:len(in_str)]
    return newstr

def Add(in_str):
    divpos = in_str.find("+")
    if divpos == -1:
        return in_str
    count_start = divpos -1
    while count_start > 0:
        if not in_str[count_start:divpos].isnumeric():
            break
        count_start -= 1
    count_end = divpos + 2
    while count_end <= len(in_str):
        if not in_str[divpos+1:count_end].isnumeric():
            count_end -= 1
            break
        count_end+= 1
    res = float(in_str[count_start:divpos])+float(in_str[divpos+1:count_end])
    newstr = in_str[0:count_start]+str(res)+ in_str[count_end:len(in_str)]
    return newstr

def Subtract(in_str):
    divpos = in_str.find("-")
    if divpos == -1:
        return in_str
    count_start = divpos -1
    while count_start > 0:
        if not in_str[count_start:divpos].isnumeric():
            break
        count_start -= 1
    count_end = divpos + 2
    while count_end <= len(in_str):
        if not in_str[divpos+1:count_end].isnumeric():
            count_end -= 1
            break
        count_end+= 1
    res = float(in_str[count_start:divpos])-float(in_str[divpos+1:count_end])
    newstr = in_str[0:count_start]+str(res)+ in_str[count_end:len(in_str)]
    return newstr  

def bracks(str_in):
    go_again = False
    i = int(0)
    brackitr_start = str_in.find("(")
    if brackitr_start == -1:
        return str_in
    i = brackitr_start+1
    
    while i < len(str_in):
        if str_in[i] == "(":
            brackitr_start = i
            #go_again = True
        elif str_in[i] == ")":
            brackitr_end = i
        i += 1
    #if go_again == True:
    #    go_again = False
    #    bracks(str_in)
    brackstr = str_in[(int(brackitr_start)+1):int(brackitr_end)]
    res = devide(brackstr)
    res = product(res)
    res = Add(res)
    res = Subtract(res)
    if brackitr_start > 0:
        newstr = str_in[0:brackitr_start-1]+str(res)+str_in[brackitr_end+1:len(str_in)]
    else:
        newstr = str(res)+str_in[brackitr_end+1:len(str_in)]
   
    return newstr
    
finres = bracks(strinput)
finres = devide(finres)
finres = product(finres)
finres = Add(finres)
finres = Subtract(finres)

print(finres)

ending = input("Please press return to continue")