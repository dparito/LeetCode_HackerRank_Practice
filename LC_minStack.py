class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack_arr = []
        

    def push(self, x: int) -> None:
        self.min_stack_arr.append(x)
        

    def pop(self) -> None:
        last_ind = len(self.min_stack_arr) - 1
        self.min_stack_arr.pop(last_ind)


    def top(self) -> int:
        last_ind = len(self.min_stack_arr) - 1
        return self.min_stack_arr[last_ind]
        

    def getMin(self) -> int:
        my_min = float('inf')
        for i in self.min_stack_arr:
            if i < my_min:
                my_min = i
        return my_min
    

    def printAll(self) -> None:
        print(*self.min_stack_arr)
        


# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(2)
minStack.printAll()
minStack.push(0)
minStack.printAll()
minStack.push(3)
minStack.printAll()
minStack.push(0)
minStack.printAll()

print(f"MIN = {minStack.getMin()}")

minStack.pop()
minStack.printAll()

print(f"MIN = {minStack.getMin()}")

minStack.pop()
minStack.printAll()

print(f"MIN = {minStack.getMin()}")

minStack.pop()
minStack.printAll()

print(f"MIN = {minStack.getMin()}")
