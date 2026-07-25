try:
    num1,num2 =  int(input("Enter two naumbers,seperated by a comma:"))
    result = num1/num2
    print("result is",result)
except ZeroDivisionError:
    print("division by zero is error !!")
except SyntaxError:
    print("comma is missing")
except :
    print("something went wrong")
else:
    print("No exceptions")
finally:
    print("executing no matter what")