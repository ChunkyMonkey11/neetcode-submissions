class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointer from back to end
        # 
        p1 = 0
        p2 = len(numbers)-1

        while p1 < p2:
            if ((numbers[p1] + numbers[p2]) == target):
                final = []
                final.append((p1+1))
                final.append(p2+1)
                return final

            if ((numbers[p1] + numbers[p2]) > target):
                p2-=1

            if ((numbers[p1] + numbers[p2]) < target):
                p1+=1