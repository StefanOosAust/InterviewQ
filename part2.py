
inputnum = 0

while inputnum != -1:
    inputnum = input("Please enter the required value (-1 to quit): ")
    thelist = list( int(x) for x in str(inputnum))
    icount = len(thelist)-1

    #numdigit = len(thelist)-1
    #inter = numdigit
    while icount > 0:
        if thelist[icount-1] > thelist[icount]:
            thelist[icount-1] = thelist[icount]
            i = icount
            while i <= (len(thelist)-1):
                thelist[i] = 9
                i +=1
        icount -= 1
    res_string = "".join(str(e) for e in thelist)
    print(int(res_string))