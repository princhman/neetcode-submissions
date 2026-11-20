class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            if nums[i] in hmap:
                hmap[nums[i]].append(i)
            else:
                hmap[nums[i]] = [i]
        
        for i in range(len(nums)):
            r = target - nums[i]
            if r == nums[i] and len(hmap[r])==2:
                return hmap[r]
            if r != nums[i] and r in hmap:
                return [i, hmap[r][0]]
