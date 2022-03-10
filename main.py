
num1 = input("enter a number: ")
num2 = input("enter another number: ")


print("1 = add")
print("2 = substract")
print("3 = multiply")
print("4 = divide")


chosen = input("chose one of the above: ")

num1_float = int(num1)
num2_float = int(num2)
chosen_float = int(chosen)

if chosen_float == 1:
    print(num1_float + num2_float)
elif chosen_float == 2:
    print(num1_float - num2_float)
elif chosen_float == 3:
    print(num1_float * num2_float)
elif chosen_float == 4:
    print(num1_float // num2_float)
else:
    print("An error occured, please try again")

