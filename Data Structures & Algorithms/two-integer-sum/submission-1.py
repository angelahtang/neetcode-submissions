class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numPointer = 0

        while numPointer < len(nums):
            runPointer = numPointer + 1

            while runPointer < len(nums):
                if nums[numPointer]+nums[runPointer] == target:
                    return [numPointer, runPointer]
                runPointer = runPointer+1
            
            numPointer = numPointer+1