vars = {}

def M(getIN):
    operation = getIN[3:]
    try:
        result = eval(operation)
        print(result)
    except (SyntaxError, NameError, TypeError, ZeroDivisionError):
        print("Invalid mathematical expression!")
def NULL():
    print("Program ended with status code '0'")
    exit()
def P(getIN):
    a = ""
    var = ""
    i = 3
    while i < len(getIN):
        if (getIN[i] == "<"):
            i += 1
            while getIN[i] != ">":
                var += getIN[i]
                i += 1
            i += 1
            a += vars[var]
        else:
            a += getIN[i]
            i += 1
    print(a)
def R(getIN):
    rLIST = []
    rIN = ""
    while rIN.split(" ")[0] != "33":
        rIN = input("")
        rLIST.append(rIN)
    for i in range(0, int(getIN.split(" ")[1])):
        flag = False
        for j in range(0, len(rLIST)):
            cond = rLIST[j].split(" ")[0]
            if cond == "80":
                P(rLIST[j])
            elif cond == "0":
                flag = True
            elif cond == "86":
                V(rLIST[j])
            elif cond == "77":
                M(rLIST[j])
        if flag:
            NULL()
def V(getIN):
    if getIN.split(" ")[2] == "61":
        a = ""
        for i in range(3, len(getIN.split(" "))):
            a += getIN.split(" ")[i] + " "
        vars[getIN.split(" ")[1]] = a[:-1]
while (True):
    getIN = input("")
    #print
    if getIN.split(" ")[0] == "80":
        P(getIN)
    elif getIN.split(" ")[0] == "0":
        NULL()
    elif getIN.split(" ")[0] == "82":
        R(getIN)
    elif getIN.split(" ")[0] == "86":
        V(getIN)
    elif getIN.split(" ")[0] == "77":
        M(getIN)
