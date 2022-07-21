class Solution:
    def util(self, pos, arr, N, res, op, target):
        if target == 0:
            res.append(op.copy())
        if pos == N:
            return
        for j in range(pos, N):
            if j != pos and arr[j] == arr[j-1]:
                continue
            if arr[j] <= target:
                op1 = op.copy()
                op1.append(arr[j])
                self.util(j+1, arr, N, res, op1, target-arr[j])

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.util(0, candidates, len(candidates), res, [], target)
        return res
