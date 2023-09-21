class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Make a hashmap to store the index of the numbers in nums. If the diff - target is in the hashmap then all we need to do is return seen[diff] and index. Otherwise we need to add the index of the num in the hashmap. 
        '''
        seen={}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], index]
            seen[num] = index


        
