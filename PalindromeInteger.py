a=int(input(""))
a=str(a)
b,c=list(a),''
b.reverse()
for i in b:
    c+=i
if a==c:
    print("True")
else:
    print("False")
    
    
