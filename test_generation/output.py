from input import main
import re
import itertools
import unittest

#lay ra phan trong docstring
def SplitDoc():
    line = main.__doc__
    return line

#Dem so bien trong phan docstring do
def CountVariables(docstring):
    ct = 0
    for w in docstring:
        if w == ":":
            ct = ct +1
    return ct

#lay ra cac so co trong moi dong cho vao list
def Createlist(value):
    l = value.split('\n')
    ls = [[]]*11
    for i in range(len(l)):
        if i!=0:
            if l[i] != None:
                ls[i-1] = [int(x.group()) for x in re.finditer(r'\d+', l[i])]
    return ls

#sap xep lai cac so trong list sao cho phan tu dau tien cua moi khoang theo thu tu tang dan
def swap(numval, ls):
    for i in range(0, numval):
        for w in range(0,len(ls[i])-2):
            if w%2==0:
                if ls[i][w]>ls[i][w+2]:
                    ls[i][w], ls[i][w+2] = ls[i][w+2], ls[i][w]
                    ls[i][w+1], ls[i][w+3] = ls[i][w+3], ls[i][w+1]
    return ls

#kiem tra xem input duoc cho co dung ko
def checkinput(numval,ls):
    check = True
    for i in range(0, numval):
        for w in range(1,len(ls[i])):
            if w%2==0:
                if ls[i][w]<=ls[i][w-1]:
                    check = False
                    break
    return check

#trong moi khoang ta lay ra 1 gia tri de test -> tao thanh 1 list cac phan tu de test
def ElementTest(numval, ls):
    khoang=[[]]*numval
    for i in range(0, numval):
        khoang[i]=[]
        for num in range(0,len(ls[i])):
            if (num % 2)==0:
                tb = (ls[i][num]+ls[i][num+1])/2
                khoang[i].append(tb)
    return khoang

#tao ra cac bo test
def CreateTest(khoang):
    #khoang = ElementTest(numval, list)
    botest1=[]
    for element in itertools.product(*khoang):
        botest1.append(element)
    casetests=[[]]*len(botest1)
    k=0
    for element in itertools.product(*khoang):
        casetests[k]=[]
        case = [k, element, "ok"]
        casetests[k].append(case)
        k+=1
    return casetests

class TestSequense(unittest.TestCase):
    pass

def test_generator(a,b):
    def test(self):
        self.assertEqual(main(*a),b)
    return test

if __name__ == '__main__':
    value = SplitDoc()
    number = CountVariables(value) #number la so bien
    listtest = swap(number, Createlist(value))
    if checkinput(number,listtest) == False:
        raise Exception("Wrong input")
    else:
        testcases = CreateTest(ElementTest(number, listtest))
        for t in testcases:
            test_name = 'test_%s' % t[0][0]
            test = test_generator(t[0][1], t[0][2])
            setattr(TestSequense, test_name, test)
        unittest.main()
