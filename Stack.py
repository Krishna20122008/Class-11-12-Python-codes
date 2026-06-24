# Stacks operations in python..

def stackpush(element,stack):
    stack.append(element)

def stackempty(stack):
    if len(stack)==0:
        return True
    else:
        return False

def stackpop(stack):
    if stackempty(stack):
        print("Underflow")
    else:
        return(stack.pop())
    
def stackview(stack):
    print(stack)

def top(stack):
    x=len(stack)
    print(f"The top element of the stack is: {stack[x-1]}")
    
stack=list()
element="Glass1"
stackpush(element,stack)

element="glass2"
stackpush(element,stack)

element="Glass3"
stackpush(element,stack)

element="Glass4"
stackpush(element,stack)

a=stackpop(stack)
print(f"The popped element from stack is: {a}")

print(stackempty(stack))

stackview(stack)

top(stack)
