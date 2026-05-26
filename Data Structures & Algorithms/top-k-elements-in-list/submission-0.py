class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num,0) + 1

        # At this point i have a frequnecy table with the frequency of each 
        # number in nums
        # Lets sort the dictonary in order of 
        frequency = dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))
        
        res = []

        for num in frequency:
            if len(res) == k:
                break
            res.append(num)
        return res