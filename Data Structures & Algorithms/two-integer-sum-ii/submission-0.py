class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx1 = 1
        idx2 = len(numbers)
        while idx1 != idx2:
            r = numbers[idx1-1] + numbers[idx2-1]
            if r == target:
                break
            elif r < target:
                idx1+=1
            elif r > target:
                idx2-=1
        return [idx1, idx2]