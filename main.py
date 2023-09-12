class Stack():
    def __init__(self):
        self.stack = []

    def iSEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.iSEmpty():
            return None
        removed = self.stack.pop()
        return removed

    def peek(self):
        return self.stack[-1] 

    def size(self):
        return len(self.stack)
    
    def __str__(self) -> str:
        return f'{self.stack}'

if __name__ == "__main__":
    stack = Stack()
    print(stack.iSEmpty())
    stack.push(1)
    stack.push(5)
    stack.push(3)
    print(stack)
    print(stack.pop())
    print(stack)
    print(stack.peek())
    print(stack.size())
    
    print()
    print('Homework 2')
    print()

    stack2 = Stack()
    couples = {'(': ')',
               '[': ']',
               '{': '}'}
    line1 = input('Введите последовательность скобок: ')
    res = 'Сбалансированно'
    for item in line1:
        if item in '([{':
            stack2.push(item)
        else:
            if stack2.iSEmpty() or couples[stack2.peek()] != item:
                res = 'Несбалансированно'
                break
            else:
                stack2.pop()
    print(res)