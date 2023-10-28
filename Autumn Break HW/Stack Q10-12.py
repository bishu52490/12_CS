
#QUES 10
stack = []

def push():
    roll = input("Enter Roll: ")
    name = input("Enter Name: ")
    stack.append((roll, name))

def pop():
    if not stack:
        print("Stack is empty")
    else:
        popped = stack.pop()
        print(f"Popped: Roll - {popped[0]}, Name - {popped[1]}")

def traverse():
    if not stack:
        print("Stack is empty")
    else:
        print("Stack contents:")
        for roll, name in stack[-1::-1]:
            print(f"Roll - {roll}, Name - {name}")

while True:
    print("\nMenu:")
    print("1. Push")
    print("2. Pop")
    print("3. Traverse")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        push()
    elif choice == '2':
        pop()
    elif choice == '3':
        traverse()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")


###Ques 11
##def push_to_stack(name):
##    if students[name] > 75:
##        stack.append(name)
##        print("Successfully pushed to Stack.")
##    else: print(name, "scored 75% or less than 75%")
##
##def pop_from_stack():
##    return stack.pop()
##
##students = {"OM": 76, "JAI": 45, "BABITA": 89, "ARUN": 65, "ANUJ": 90, "TARUN": 82}
##stack = []
##
##for name in students:
##    push_to_stack(stack, name)
##
##for choice=='2'
##    if stack:
##        popped_item = pop_from_stack(stack)
##        print(f"Popped item: {popped_item}")
##    else:
##        print("Stack is empty")
##
### Display updated stack contents
##print("\nUpdated Stack:")
##display_stack(stack)
##
##    
##
##
