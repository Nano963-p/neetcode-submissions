class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack = []
    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.minstack.append(val)
        else :
            if val <= self.minstack[-1] :
                self.minstack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        num = self.stack.pop()
        if num == self.minstack[-1] :
            self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1] 

    def getMin(self) -> int:
        return self.minstack[-1]
