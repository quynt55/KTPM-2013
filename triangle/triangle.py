def checkInput(a,b,c):
    if((type(a) in [int, float, long]) and(type(b) in [int, float, long]) and (type(c) in [int, float, long]) and (a>0) and (b>0) and (c>0) ):
        return 1
    else:
        return 0
def detect_triangle(a,b,c):
    if(checkInput(a,b,c) == 0 ):
        return "Nhap sai"
    else:
        if( (a + b) <= c)or((a+c)<=b)or((b+c)<=a):
            return "Khong phai la ba canh tam giac!"
        elif((a==b)and(b==c)and(a==c)):
            return "Tam giac deu"
        elif((a==b)or(a==c)or(b==c)):
            if(((a*a+b*b)-c*c) <= 10**-9 or((a*a + c*c)-b*b)<= 10**-9 or((b*b + c*c) - a*a)<=10**-9):
                return "Tam giac vuong can"
            else:
                return "Tam giac can"
        elif(((a*a+b*b)==c*c)or((a*a + c*c)==b*b)or((b*b + c*c) == a*a)):
            return "Tam giac vuong"
        else:
            return "Tam giac thuong"
#if __name__=="__main__":
#    a=float(raw_input())
#    b=float(raw_input())
#    c=float(raw_input())
#    detect_triangle(a,b,c);
