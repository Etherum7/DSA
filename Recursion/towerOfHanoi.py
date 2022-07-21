class Solution:
    def toh(self, N, fromm, to, aux):
        # Your code here
        
        def util( N, fromm, to, aux, c):
            c[0]+=1
            if N==1:
                print('move disk 1 from rod '+str(fromm)+' to rod '+str(to))
                return

            util(N-1, fromm, aux, to,c)
            print("move disk "+str(N)+" from rod "+str(fromm)+" to rod "+str(to))
            util(N-1, aux, to, fromm,c)
        c=[0]
        util(N, fromm, to, aux, c)
        return c[0]
        