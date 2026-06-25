# Queue operations in python..

def isempty(queue):
    if len(queue)==0:
        return True
    else: return False

def push(element,queue):
    queue.append(element)

def pop(queue):
    z=queue.pop(0)
    print(z)

def view(queue):
    print(queue)

queue=list()
print(isempty(queue))

a="Kishan"
push(a,queue)

a="Swapnil"
push(a,queue)

a="Cheryl"
push(a,queue)

a="Krishna"
push(a,queue)

pop(queue)

pop(queue)


view(queue)

print(f"Is the queue empty now?: {isempty(queue)}")