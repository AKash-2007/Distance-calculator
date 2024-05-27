print(" "*20,"DISTANCE CALCULATOR\n"," "*19,"-"*19)
while True:
    x1,y1=map(int,input("\nEnter point 1's co-ordinate: ").split(","))
    x2,y2=map(int,input("Enter point 2's co-ordinate: ").split(","))
    distance=round(((x2-x1)**2+(y2-y1)**2)**0.5,3)
    print("Distance between two points=",distance)
    print(" "*28,len(str(distance))*"-")
    a=input("Do you want to continue or exit? (yes/no):  ")
    if a=="no":
        print("Thank you")
        break
