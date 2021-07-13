import datetime
def server_cost(d1, m1, y1, d2, m2, y2):
    x1=datetime.datetime(y1,m1,d1)
    x2=datetime.datetime(y2,m2,d2)
    if y2-y1==0:
        no=(((y2-y1)*365)+int(x2.strftime("%j"))-int(x1.strftime("%j"))) #no is number of days
    else:
        no=(365-int(x1.strftime("%j"))+((y2-y1-1)*365)+int(x2.strftime("%j")))
    print(no)
    if no==0:
        return 20
    elif (no/30)<=1:
        return no*30
    elif (no/30)>1 and (no/30)<=12:
        return (no//30)*1000
    elif (no/365)>1:
        return 20000
    
if __name__ == '__main__':
    d1M1Y1 = input().split()
    d1 = int(d1M1Y1[0])
    m1 = int(d1M1Y1[1])
    y1 = int(d1M1Y1[2])

    d2M2Y2 = input().split()
    d2 = int(d2M2Y2[0])
    m2 = int(d2M2Y2[1])
    y2 = int(d2M2Y2[2])

    result = server_cost(d1, m1, y1, d2, m2, y2)
    print(str(result) + '\n')
    
