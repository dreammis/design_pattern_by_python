class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        try:
            return self.items[-1]
        except IndexError:
            raise ("Stack is empty!")


class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.insert(0, value)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)



def parChecker(symbolString):
    s = Stack()
    balance = True

    for value in symbolString:
        if value == "(":
            s.push(value)
        else:
            if s.isEmpty():
                balance = False
            else:
                s.pop()
    return balance and s.isEmpty()

print(parChecker("((()))"))


def hotPotato(children, num):
    queue = Queue()

    for child in children:
        queue.enqueue(child)

    while queue.size() > 1:
        [queue.enqueue(queue.dequeue()) for i in range(num)]
        queue.dequeue()
    return queue.dequeue()

print(hotPotato(['a', 'b', 'c', 'd', 'e', 'f'], 7))








