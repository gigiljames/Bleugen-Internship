#doesn't work for all cases
a,b,c,d=str(input("")),['()','{}','[]'],1,1
if a.isalnum()==True or len(a)%2==1:
    c=0
else:
    for i in range(0,len(a),2):
        if a[i]+a[i+1] in b:
            c*=1
        else:
            c*=0
    if c!=1:
        for i in range(0,len(a)//2):
            if a[i]+a[-(i+1)] in b:
                d*=1
            else:
                d*=0            
if c==1 or d==1:
    print("True")
else:
    print("False")




    
