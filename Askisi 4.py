text = []
num1 = []
result =  0
position = 0
numberone = ""
praksi=""
numberthree=""
kimeno = input("dwse praksi")
plithos = len(kimeno)
def zero():
    return 0
def one():
    return 1
def two():
    return 2
def three():
    return 3
def four():
    return 4
def five():
    return 5
def six():
    return 6
def seven():
    return 7
def eight():
    return 8
def nine():
    return 9
def plus(a,b):
    return a + b
def minus(a,b):
    return a - b
def times(a,b):
    return a * b
def find (arithmos):
    x=10
    if (arithmos == "zero"):
        x = zero()
    elif (arithmos == "one"):
        x = one()
    elif (arithmos == "two"):
        x = two()
    elif (arithmos == "three"):
        x = three()
    elif (arithmos == "four"):
        x = four()
    elif (arithmos == "five"):
        x = five()
    elif (arithmos == "six"):
        x = six()
    elif (arithmos == "seven"):
        x = seven()
    elif (arithmos == "eight"):
        x = eight()
    elif (arithmos == "nine"):
        x = nine()

    return x


for i in range(plithos):
    text.append(kimeno[i])
for i in range(text.__len__()):

    if (text[i]=='(') and (text[i] != ')'):
        position = i +1
        break
    num1.append(text[i])
num2 = []
for i in range(position, text.__len__()):
    if (text[i]== '(') and (text[i] != ')'):
        position = i +1
        break
    num2.append(text[i])
num3 = []
for i in range(position, text.__len__()):
        if (text[i] == '(') and (text[i] != ')'):
            position = i + 1
            break
        num3.append(text[i])
for i in range(0,num1.__len__()):
    numberone = numberone + num1[i]


for i in range(0,num2.__len__()):
    praksi = praksi + num2[i]


for i in range(0,num3.__len__()):
    numberthree = numberthree + num3[i]

a = find(numberone)
b = find(numberthree)

if (praksi == "plus"):
    result = plus(a,b)
elif (praksi == "minus"):
    result = minus(a,b)
elif (praksi == "times"):
    result = times(a, b)

print (result)






