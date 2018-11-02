class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            # ^ 异或，转换成二进制数字后按位求异或
            res ^= num
            print(res)
        return res

if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,2,4,4]
    print(solution.singleNumber(nums))