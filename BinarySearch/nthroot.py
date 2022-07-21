def findNthRootOfM(n, m):
    # Write your Code here.
    eps = 1e-7
    start = 1.0
    end = float(m)
    guess = (start+end)/2
#     val = guess**n
    while abs((guess**n)-m) > eps:
        if guess**n < m:
            start = guess
        else:
            end = guess
        guess = (end+start)/2
        
    return format(guess, '.6f')
'''
    Time Complexity: O(log(M) * log(N)):
    Space Complexity: O(1):
    
    Where N and M are given integers.
'''

def findNthRootOfM(n,m):
    
    # Variable to store maximum possible error in order
    # to obtain the precision of 10 ^ (-6) in the answer.
    error = 1/10**7

    # Difference between the current answer, and the answer
    # in next iteration, which we take as big as possible initially.
    diff = 10**18

    # Guessed answer value
    xk = 2

    # We keep on finding the precise answer till the difference between
    # answer of two consecutive iteration become less than 10^(-7).
    while (diff > error):

        # Answer value in the next iteration.
        xk_1 = (pow(xk, n) * (n - 1) + m) / (n * pow(xk, n - 1))
        
        # Difference of answer in consecutive states updated.
        diff = abs(xk - xk_1)
        
        # Updating the current answer with the answer of next iteration.
        xk = xk_1
    
    # Returning the nthRootOfM with precision upto 6 decimal places
    # which is xk.
    xk=round(xk,6)
    return format(xk, '.6f')