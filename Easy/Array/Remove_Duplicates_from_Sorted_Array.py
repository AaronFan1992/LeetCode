class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        newTail = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[newTail]:
                newTail += 1
                nums[newTail] = nums[i]

        return newTail + 1

if __name__ == "__main__":
    solution = Solution()
    nums = [1,1,2,3,3,4]
    print(solution.removeDuplicates(nums))