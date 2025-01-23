x1,y1=10,20
x2,y2=20,30
x3,y3=30,40
area=x1*(x2*y3-y2*x3)-x2*(x1*y3-y1*x3)+x3*(x1*y2-y1*x2)
if(area==0):
    print("they lie on same line")
else:
    print("they dt lie on same line")
