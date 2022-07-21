class Solution:
    def util(self, i, arr, res, N, op, target):
        if i > N:
            return
        if i == N and target == 0:
            res.append(op)
            return
        if i == N:
            return
        if arr[i] <= target:
            op1 = op.copy()
            op1.append(arr[i])
            self.util(i, arr, res, N, op1, target-arr[i])
        self.util(i+1, arr, res, N, op, target)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        N = len(candidates)
        self.util(0, candidates, res, N, [], target)
        return res
