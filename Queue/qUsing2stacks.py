# User function Template for python3
class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        if len(self.output) == 0:
            while len(self.input):
                self.output.append(self.input.pop())
        if len(self.output):
            return self.output.pop()
        return -1

    def peek(self) -> int:
        if len(self.output):
            return self.output[-1]
        if len(self.input):
            return self.input[0]
        return -1

    def empty(self) -> bool:
        return len(self.input)+len(self.output) == 0
# Function to push an element in queue by using 2 stacks.


def Push(x, stack1, stack2):
    '''
    x: value to push
    stack1: list
    stack2: list
    '''
    # stack1.append(x)
    while len(stack1):
        stack2.append(stack1.pop())
    stack1.append(x)
    while len(stack2):
        stack1.append(stack2.pop())

    # code here

# Function to pop an element from queue by using 2 stacks.


def Pop(stack1, stack2):
    '''
    stack1: list
    stack2: list
    '''
    # print(stack1, stack2)
    if len(stack1):
        return stack1.pop()
    else:
        return -1
    # code here

# {
#  Driver Code Starts
# Initial Template for Python 3


# contributed by RavinderSinghPB
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        qry = int(input())
        qtyp_qry = list(map(int, input().strip().split()))

        i = 0
        stack1 = []
        stack2 = []
        while i < len(qtyp_qry):
            # print(i)
            if qtyp_qry[i] == 1:
                Push(qtyp_qry[i+1], stack1, stack2)
                # print(i)
                i += 2
            else:
                print(Pop(stack1, stack2), end=' ')
                i += 1

        print()
# } Driver Code Ends
