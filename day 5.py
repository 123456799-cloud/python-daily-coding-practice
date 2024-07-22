marks = int (input("ENTER THE MARKS"))
#statement

if marks >=90 and marks<=100:
    print("congratulation you got a 'A'Grade")
elif marks>=80 and marks<=90:
    print( "congratulation you got a 'B'Grade")
elif marks>=70 and marks <=80:
    print("congratulation you got a 'C'Grade")
elif marks>=60 and marks <=70:
    print("congratulation you got a 'D'Grade")
elif marks>=40 and marks <=70:
    print(" congratulation you got a 'E'Grade")
    
elif marks<40:
    print("  Sorry you are fail ,please try hard next time")
else:
    print("please enter your valid marks")