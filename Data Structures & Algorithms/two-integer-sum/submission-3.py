class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Two indicies being returned may never be the same. 
        complements = {}
        for i,v in enumerate(nums):
            complement = target - v
            if complement in complements.keys():
                    return [complements[complement],i]
            else:
                complements[v] = i