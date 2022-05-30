a = int(input("enter number of rectangles"))
for i in range (a):
    p = list(map(float,input().split()))
    x1,y1,x2,y2,x3,y3 = p[0],p[1],p[2],p[3],p[4],p[5]
    area = (x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
    if (area < 0):
        print(f"Area of rectangle with vertices ({x1},{y1}),({x2},{y2}),({x3},{y3})is",area*(-1))
    else:
        print(f"Area of rectangle with vertices ({x1},{y1}),({x2},{y2}),({x3},{y3})is",area)