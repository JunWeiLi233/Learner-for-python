#Exception: ZeroDivisionError, TypeError, ValueError

# 1 + "1" #TypeError
# int("Pizza") #ValueError

#Exception handling= try + except + finally

# number = int(input("Enter a number: "))
# print(1 / number) #Zero/String -> error

try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Enter only numbers pleased!")
except Exception:
    print("Something went wrong!")
finally:
    print("Do some cleanup here")


#except Exception -> catch all exceptions but too broad


