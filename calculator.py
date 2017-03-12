import re

print("Welcome to the Magical Python Calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True
#set previous to zero because we have not done any math yet!

def perform_math():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter equation: ")
    else:
        equation = input(str(previous))

    if equation == 'quit':
        run = False
        print("Goodbye, human.")
    else:
        equation = re.sub('[a-zA-Z.,:()" "]', '', equation)
        #eval is dangerous when left to humans, let's make sure only numbers and mathmatical opperators are accepted

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

while run:
    perform_math()
