class Stack:
    def __init__(self):
        self.arr = [0]
        self.max_element = [0]

    def push(self,data):
        self.arr.append(data)
        if self.max[-1] <= data:
            self.max_element.append(data)

    def pop(self):
        if self.arr[-1] == self.max_element[-1]:
            self.max_element.pop()
        self.arr.pop()


input_ = int(input())
stack_ = Stack()
for i in range(input_):
    x = str(input())
    if x[0] == "1":
        stack_.push(int(x[2:]))
    elif x[0] == "2":
        stack_.pop()
    else:
        print(stack_.max_element[-1])