try:
    number = int(input("Enter a number: "))
except ValueError as ex:
    print("exception:", ex)