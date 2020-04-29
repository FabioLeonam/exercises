class Conversion:
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.input = []
        self.output = []
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False
    
    def peek(self):
        return self.input[-1]

    def pop(self):
        if not self.is_empty():
            self.top -= 1
            return self.input.pop()
        else:
            return "$"
    
    def push(self, operator):
        self.top += 1
        self.input.append(operator)

    def is_operand(self, character):
        return character.isalpha()

    #Check if the precedence of operator is strictly
    #less tha top of stack
    def not_greater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            if a <= b:
                return True
            else:
                return False
        except KeyError:
            return False

    def infix_to_postfix(self, expression):
        for i in expression:
            if self.is_operand(i):
                self.output.append(i)
            elif i == '(':
                self.push(i)
            # If the scanned character is an ')', pop and  
            # output from the stack until and '(' is found
            elif i == ')':
                while((not self.is_empty()) and self.peek() != '('):
                    a = self.pop()
                    self.output.append(a)
                if(not self.is_empty() and self.peek() != '('):
                    return -1
                else:
                    self.pop()
            # An operator is found
            else:
                while(not self.is_empty() and self.not_greater(i)):
                    self.output.append(self.pop())
                self.push(i)
        
        while not self.is_empty():
            self.output.append(self.pop())
        
        print("".join(self.output))
        

expression = "(a*b)+c/d+(e*b)" #Expected output: abc*+d+
obj = Conversion(len(expression))
obj.infix_to_postfix(expression)


