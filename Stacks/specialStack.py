class SpecialStack():
    def __init__(self):
        self.st=[]
        self.ss=[]
    def push(self, ele):
        self.st.append(ele)
        if len(self.ss==0):
            self.ss.append(ele)
        elif ele< self.ss[-1]:
            self.ss.append(ele)

    def pop(self):
        if len(self.st) :

            val= self.st.pop()
            if len(self.ss) and val== self.ss[-1]:
                self.ss.pop()
            return val
        return -1
    def getMin(self):
        return self.ss[-1]

    