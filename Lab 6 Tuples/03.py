def isleap(y):
    return y%4==0 and (y%100!=0 or y%400==0)
def daysInM(m,y):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if m==2 and isleap(y):
        return 29
    return days[m-1]
def dayDiff(d1,d2):
    c=0
    d,m,y=d1
    d_,m_,y_=d2
    while y<y_ or (y==y_ and m<m_ ) or (y==y_ and m==m_ and d<d_):
        c+=1
        d+=1
        if d>daysInM(m,y):
            d=1
            m+=1
        if m>12:
            m=1
            y+=1
    return c

d1=(1,1,2024)
d2=(3,1,2024)
print(dayDiff(d1,d2))